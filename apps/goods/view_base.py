from django.views.generic.base import View
from django.forms.models import model_to_dict
from django.core import serializers

from .models import Goods
from django.http import HttpResponse, JsonResponse
import json


class GoodsListView(View):

    def get(self, request):

        # list_dict = []
        goods = Goods.objects.all()[:10]
        # for good in goods:
        #     # goods_dict = {}
        #     # goods_dict["name"] = good.name
        #     # goods_dict["category"] = good.goods_category.name
        #     # goods_dict["market_price"] = good.market_price
        #     goods_dict = model_to_dict(good)
        #     list_dict.append(goods_dict)
        list_dict = serializers.serialize("json", goods)
        list_dict = json.loads(list_dict)
        return JsonResponse(list_dict, safe=False)
        # return HttpResponse(list_dict, content_type="application/json")