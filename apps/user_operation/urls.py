from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
from .views import UserFavViewSet, UserMessageViewSet, UserAddressViewSet

router = DefaultRouter()
router.register(r"user_fav", UserFavViewSet, base_name="user_fav")
router.register(r"user_message", UserMessageViewSet, base_name="user_message")
router.register(r"user_address", UserAddressViewSet, base_name="user_address")

urlpatterns = [
    re_path(r"^", include(router.urls)),
]