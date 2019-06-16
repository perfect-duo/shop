from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from .models import Goods, GoodsCategory, GoodsBanner
from .serializers import GoodsSerializer, GoodsCategorySerializer, GoodBannerSerializer, IndexGoodsSerializer
from .filters import GoodsFilter
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = "p"


class GoodsApiView(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    商品列表， 包括商品的分页， 搜索， 查询  排序
    """

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    throttle_classes = (AnonRateThrottle, UserRateThrottle)
    pagination_class = LargeResultsSetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ('name', "market_price")
    filterset_class = GoodsFilter
    search_fields = ("^name", "goods_brief")
    ordering_fields = "sold_num"      #('market_price', 'name')
    # def get_queryset(self):
    #     queryset = Goods.objects.all()
    #     prices = self.request.query_params.get("price", 0)
    #     if prices:
    #         queryset = queryset.filter(market_price__gt=int(prices))
    #     return queryset

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    # def get(self, request, format=None):
    #     goods = Goods.objects.all()[:10]
    #     goods_serializer = GoodsSerializer(goods, many=True)
    #     return Response(goods_serializer.data)


class GoodsCategoryView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    """
    商品所属类型
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = GoodsCategorySerializer


class GoodsBannerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    首页轮播图
    """
    queryset = GoodsBanner.objects.all()[:4]
    serializer_class = GoodBannerSerializer


class IndexGoodsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    首页显示最新上架商品
    """
    queryset = GoodsCategory.objects.filter(is_tab=True)
    serializer_class = IndexGoodsSerializer


