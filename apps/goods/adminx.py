import xadmin
from goods.models import Goods, GoodsCategory, GoodsBrand, GoodsBanner, GoodImages


class Goods_Images(object):
    model = GoodImages
    extra = 0


class GoodsAdmin(object):

    list_display = ("goods_category", "goods_number", "name", "click_num", "sold_num", "fav_num",
                    "goods_num", "market_price", "shop_price", "goods_brief", "goods_desc", "transportation_price",
                    "goods_front_images", "is_new", "add_time")
    search_field = ("goods_category", "goods_number", "name", "click_num", "sold_num", "fav_num",
                    "goods_num", "market_price", "shop_price", "goods_brief", "goods_desc", "transportation_price",
                    "goods_front_images", "is_new")
    list_filter = ("goods_category", "goods_number", "name", "click_num", "sold_num", "fav_num",
                    "goods_num", "market_price", "shop_price", "goods_brief", "goods_desc", "transportation_price",
                    "goods_front_images", "is_new", "add_time")
    inlines = [Goods_Images]
    data_charts = {
        "goods": {'title':"商品分析", "x-field": "goods_num", "y-field": ("market_price",), "order": ("goods_num",)}
    }




class GoodsCategoryAdmin(object):
    list_display = ("name", "code", "desc", "category_type", "parent_category", "is_tab", "add_time")
    search_field = ("name", "code", "desc", "category_type", "parent_category", "is_tab")
    list_filter = ("name", "code", "desc", "category_type", "parent_category", "is_tab", "add_time")


class GoodsBrandAdmin(object):
    list_display = ("name", "desc", "image", "add_time")
    search_field = ("name", "desc", "image")
    list_filter = ("name", "desc", "image", "add_time")


class GoodsImagesAdmin(object):
    list_display = ("goods", "images", "add_time")
    search_field = ("goods", "images")
    list_filter = ("goods", "images", "add_time")


class GoodsBannerAdmin(object):
    list_display = ("goods", "images", "index", "add_time")
    search_field = ("goods", "images", "index")
    list_filter = ("goods", "images", "index", "add_time")


xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(GoodsBrand, GoodsBrandAdmin)
xadmin.site.register(GoodImages, GoodsImagesAdmin)
xadmin.site.register(GoodsBanner, GoodsBannerAdmin)