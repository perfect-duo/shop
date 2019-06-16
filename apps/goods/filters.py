from django_filters import rest_framework
from django.db.models import Q
from .models import Goods


class GoodsFilter(rest_framework.FilterSet):
    min_price = rest_framework.NumberFilter(field_name="market_price", lookup_expr='gte')
    max_price = rest_framework.NumberFilter(field_name="market_price", lookup_expr='lte')
    name = rest_framework.CharFilter(field_name="name", lookup_expr="icontains")
    top_category = rest_framework.NumberFilter(method="top_category_filter")

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(goods_category__id=value)|Q(goods_category__parent_category__id=value)|Q(goods_category__parent_category__parent_category__id=value))

    class Meta:
        model = Goods
        # fields = ["min_price", "max_price", "name"]
        # fields = {
        #     "shop_price": ["lt", "gt"]
        # }
        fields = ['is_new']