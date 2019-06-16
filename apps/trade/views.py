from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from trade.serializers import ShopCarSerializer, ShopCarReturnSerializer, ShopOrderSerializer, ShopOrderSerializer2
from .models import ShoppingCat, OrderForm, OrderGoods
from rest_framework.views import APIView
from django.shortcuts import redirect
from alipay import AliPay
from shop.settings import ALIPAY_PRIVATE, ALIPAY_PUBLIC
from rest_framework.response import Response
from urllib.parse import urlparse, parse_qs
# Create your views here.


class UserShopCar(viewsets.ModelViewSet):
    """
    用户购物车

    list:
        用户购物车列表
    create:
        用户点击购物
    delete:
        用户删除购物物品

    """

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    lookup_field = "goods_id"
    # serializer_class = ShopCarSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ShopCarReturnSerializer
        else:
            return ShopCarSerializer

    def get_queryset(self):
        return ShoppingCat.objects.filter(user=self.request.user)


class ShopOrderViewSet(viewsets.ModelViewSet):
    """
    list:
        所有订单的显示
    create:
        订单的生成
    delete:
        订单的删除

    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = ShopOrderSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ShopOrderSerializer2
        else:
            return ShopOrderSerializer

    def get_queryset(self):
        return OrderForm.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        order = serializer.save()
        goods = ShoppingCat.objects.filter(user=self.request.user)

        for gd in goods:

            # 生成订单商品
            shop_goods = OrderGoods()
            shop_goods.order_form = order
            shop_goods.goods = gd.goods
            shop_goods.num = gd.nums
            shop_goods.save()

            # 清空购物车
            gd.delete()


        # shop_goods.order_form = serializer
        # shop_goods.goods = serializer.shop_car


class AliPayApiView(APIView):
    """
     支付宝响应接口
    """
    def get(self, request):
        """
        支付宝 return_url 的同步跳转地址
        :param request:
        :return:
        """

        return redirect("http://192.168.27.53:8000/trade/shop_order/")

    def post(self, request):
        """
        支付宝服务器主动通知商户服务器， 异步回调
        :param request:
        :return:
        """
        alipay_dict = {}
        for k , v in request.POST.items():
            alipay_dict[k] = v
        signature = alipay_dict.pop("sign")

        alipay = AliPay(
            appid="2016092000552511",
            app_notify_url="https://192.168.27.53：8000/return/alipay/",
            app_private_key_path=ALIPAY_PRIVATE,
            alipay_public_key_path=ALIPAY_PUBLIC,
            sign_type="RSA2",
            debug=True,

        )

        success = alipay.verify(alipay_dict, signature)
        if success:   # and data["trade_status"] in ("TRADE_SUCCESS", "TRADE_FINISHED"):
            no = OrderForm.objects.filter(order_no=alipay_dict["out_trade_no"])
            if no:
                for n in no:
                    n.trade_no = alipay_dict["trade_no"]
                    n.pay_status = alipay_dict["pay_status"]
                    n.pay_time = alipay_dict["timestamp"]
                    n.save()
                return Response("success")





