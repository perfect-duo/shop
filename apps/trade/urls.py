from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
from .views import UserShopCar, ShopOrderViewSet, AliPayApiView
router = DefaultRouter()
router.register(r"shop_car", UserShopCar, base_name="shop_car")
router.register(r"shop_order", ShopOrderViewSet, base_name="shop_order")

urlpatterns = [
    re_path(r"^return/alipay/$", AliPayApiView.as_view(), name="return_alipay"),
    re_path("^", include(router.urls)),
]