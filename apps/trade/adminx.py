import  xadmin
from trade.models import ShoppingCat, OrderForm, OrderGoods


class ShoppingCatAdmin(object):
    list_display = ("user", "goods", "nums", "money", "add_time")
    search_field = ("user", "goods", "nums", "money")
    list_filter = ("user", "goods", "nums", "money", "add_time")


class OrderFormAdmin(object):
    list_display = ("user", "shop_cat", "order_no", "trade_no", "pay_status", "post_script", "order_mount",
                    "pay_time", "address", "signer_name", "signer_mobile", "add_time")
    search_field = ("user", "shop_cat", "order_no", "trade_no", "pay_status", "post_script", "order_mount",
                    "pay_time", "address", "signer_name", "signer_mobile")
    list_filter = ("user", "shop_cat", "order_no", "trade_no", "pay_status", "post_script", "order_mount",
                    "pay_time", "address", "signer_name", "signer_mobile", "add_time")


class OrderGoodsAdmin(object):
    list_display = ("order_form", "goods", "num", "add_time")
    search_field = ("order_form", "goods", "num")
    list_filter = ("order_form", "goods", "num", "add_time")


xadmin.site.register(ShoppingCat, ShoppingCatAdmin)
xadmin.site.register(OrderForm, OrderFormAdmin)
xadmin.site.register(OrderGoods, OrderGoodsAdmin)