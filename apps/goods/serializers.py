from rest_framework import serializers
from .models import Goods, GoodsCategory, GoodImages, GoodsBanner, GoodsBrand
from django.db.models import Q


class GoodsCategorySerializer3(serializers.ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsCategorySerializer2(serializers.ModelSerializer):
    sub_cut = GoodsCategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsCategorySerializer(serializers.ModelSerializer):
    sub_cut = GoodsCategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodImages
        fields = ("images",)


class GoodsSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=100, required=True)
    # click_num = serializers.IntegerField(default=0)
    # goods_front_images = serializers.ImageField()

    # def create(self, validated_data):
    #     return Goods.objects.create(**validated_data)
    goods_category = GoodsCategorySerializer()
    different_images = GoodsImagesSerializer(many=True)

    class Meta:
        model = Goods
        fields = "__all__"


class GoodBannerSerializer(serializers.ModelSerializer):

    """
    商品轮播图
    """
    class Meta:
        model = GoodsBanner
        fields = ("goods", "images", "index")


class GoodsBandSerializer(serializers.ModelSerializer):
    """
    商品品牌
    """
    class Meta:
        model = GoodsBrand
        fields = "__all__"


class IndexGoodsSerializer(serializers.ModelSerializer):
    """
    商品首页显示的商品，商品类型
    """
    goods_band = GoodsBandSerializer(many=True)
    goods = serializers.SerializerMethodField()
    sub_cut = GoodsCategorySerializer2(many=True)

    def get_goods(self, obj):
        goods = Goods.objects.filter(Q(goods_category__id=obj.id)|Q(goods_category__parent_category__id=obj.id)
                             |Q(goods_category__parent_category__parent_category__id=obj.id))
        serializers = GoodsSerializer(goods, many=True, context={"request": self.context["request"]})
        return serializers.data

    class Meta:
        model = GoodsCategory
        fields = "__all__"





