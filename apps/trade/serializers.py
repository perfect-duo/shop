from rest_framework import serializers
from goods.models import Goods
from .models import ShoppingCat, OrderForm, OrderGoods
from random import randint
from datetime import datetime
import re
from alipay import AliPay
from shop.settings import VERIFY_MOBILE, ALIPAY_PRIVATE, ALIPAY_PUBLIC


class ShopCarSerializer(serializers.Serializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    goods = serializers.PrimaryKeyRelatedField(required=True, queryset=Goods.objects.all())
    nums = serializers.IntegerField(min_value=1, required=True, error_messages={
                                            "min_value": "商品数量不能小于 1", "required": "请选择购买数量"
                                            })

    # money = serializers.IntegerField(default=0)
    money = serializers.IntegerField(default=0)

    def create(self, validated_data):

        user = self.context["request"].user
        goods = self.validated_data["goods"]
        num = self.validated_data["nums"]
        shop_car = ShoppingCat.objects.filter(user=user, goods=goods)

        if shop_car:
            shop_car[0].nums += num
            shop_car[0].save()
            # return ShoppingCat. objects.create(user=user, goods=goods, nums=)
        else:
            shop_car[0] = ShoppingCat.objects.create(**validated_data)

        return shop_car[0]

    def update(self, instance, validated_data):

        instance.nums = validated_data["nums"]
        instance.save()
        return instance


class GoodsSerializer(serializers.ModelSerializer):
    """
    为了内嵌购物车而使用
    """
    class Meta:
        model = Goods
        fields = "__all__"


class ShopCarReturnSerializer(serializers.ModelSerializer):
    """
    返回前端的serializer
    """
    goods = GoodsSerializer()

    class Meta:
        model = ShoppingCat
        fields = "__all__"
        # exclude = ("")


class ShopOrderSerializer(serializers.ModelSerializer):
    """
    生成订单的 serializer
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    add_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M")
    order_no = serializers.CharField(read_only=True)
    pay_time = serializers.DateTimeField(read_only=True)
    pay_status = serializers.CharField(read_only=True)
    trade_no = serializers.CharField(read_only=True)
    alipay_url = serializers.SerializerMethodField(read_only=True)
    # order_mount = serializers.FloatField(read_only=True, help_text="订单金额")

    def get_alipay_url(self, obj):
        """
        生成支付宝链接支付url
        :param obj:
        :return:
        """
        alipay = AliPay(
            appid="2016092000552511",
            app_notify_url="https://192.168.27.53：8000/return/alipay/",
            app_private_key_path=ALIPAY_PRIVATE,
            alipay_public_key_path=ALIPAY_PUBLIC,
            sign_type="RSA2",
            debug=True,
        )
        url = alipay.api_alipay_trade_page_pay(
            subject=obj.order_no,
            out_trade_no=obj.order_no,
            total_amount=obj.order_mount,
            return_url="https://192.168.27.53：8000/return/alipay/",
            )
        re_url = "https://openapi.alipaydev.com/gateway.do?{date}".format(date=url)
        return re_url

    def validate_signer_mobile(self, data):

        if not re.match(VERIFY_MOBILE, data):
            raise serializers.ValidationError("手机号格式不正确")
        return data

    def get_order_no(self):
        return "{time_str}{user_id}{random}".format(time_str=datetime.now().strftime("%Y%m%d%H%M%S"),
                                                    user_id=self.context["request"].user.id,random=randint(10, 99))

    def validate(self, attrs):
        attrs["order_no"] = self.get_order_no()
        return attrs

    class Meta:
        model = OrderForm
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    """
    订单商品
    """
    goods = GoodsSerializer(many=False)

    class Meta:
        model = OrderGoods
        fields = "__all__"


class ShopOrderSerializer2(serializers.ModelSerializer):
    """
    获取订单详情
    """
    order_goods = OrderSerializer(many=True)

    class Meta:
        model = OrderForm
        fields = "__all__"








