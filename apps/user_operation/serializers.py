from rest_framework import serializers
from .models import UserFav, UserMessage, UserAddress
from goods.models import Goods
import re
from shop.settings import VERIFY_MOBILE


class UserFavSerializers(serializers.ModelSerializer):
    """
        用户收藏
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserFav
        fields = ("user", "goods", "id")


class GoodsSerializer(serializers.ModelSerializer):
    """
    用户商品作为用户收藏嵌套
    """
    class Meta:
        model = Goods
        fields = "__all__"


class UserFavDetailSerializer(serializers.ModelSerializer):
    """
    用户收藏列表
    """
    goods = GoodsSerializer()

    class Meta:
        model = UserFav
        fields = ("goods", "id")


class UserMessageSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    add_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H-%M")

    class Meta:
        model = UserMessage
        fields = ("user", "message_type", "theme", "message", "files", "id", "add_time")


class UserAddressSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserAddress
        fields = ("user", "name", "address", "detail_address", "mobile", "id")

    def validate_mobile(self, attrs):
        """
        验证手机号是否合法

        """
        if not re.match(VERIFY_MOBILE, attrs):
            raise serializers.ValidationError("请输入正确的手机号")

        return attrs
