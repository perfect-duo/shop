import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")


import django
django.setup()


from goods.models import GoodsCategory, Goods, GoodImages
from db_tools.data.product_data import row_data


for goods_detail in row_data:
    goods = Goods()

    goods.name = goods_detail["name"]
    goods.market_price = goods_detail["market_price"]
    goods.shop_price = goods_detail['sale_price']
    if goods_detail["desc"]:
        goods.goods_brief = goods_detail["desc"]
    else:
        goods.goods_brief = " "
    goods.goods_desc = goods_detail["goods_desc"]
    goods.goods_front_images = goods_detail["images"][0]

    category = goods_detail["goods_category"][-1]
    gc = GoodsCategory.objects.filter(name=category)
    if gc:
        goods.goods_category = gc[0]
    goods.save()

    for goods_images in goods_detail["images"]:
        goodsimages = GoodImages()
        goodsimages.images = goods_images
        goodsimages.goods = goods

        goodsimages.save()







