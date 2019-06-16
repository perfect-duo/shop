from django.urls import re_path, include
from goods.view_base import GoodsListView
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from goods.views import GoodsApiView, GoodsCategoryView, GoodsBannerViewSet, IndexGoodsViewSet
from rest_framework.routers import DefaultRouter

#
router = DefaultRouter()
router.register(r"goods", GoodsApiView, base_name="goods")
router.register(r"category", GoodsCategoryView, base_name="category")
router.register(r"banner", GoodsBannerViewSet, base_name="banner")
router.register(r"index_category", IndexGoodsViewSet, base_name="index_category")
# user_list = GoodsApiView.as_view({
#         'get': 'list'
#                         })
urlpatterns = [
        # re_path(r"goods_list/$", GoodsListView.as_view()),
        # re_path(r"goods_list/$", GoodsApiView.as_view()),
        # re_path(r"goods_lists/$", user_list),
        re_path(r"^", include(router.urls)),
        re_path(r'^api-token-auth/',  views.obtain_auth_token),
        re_path(r'^login/$', obtain_jwt_token),

]