from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
from users.views import SmsUserProfile, RegisterViewSet, UserDetailViewSet


router = DefaultRouter()
router.register(r"code", SmsUserProfile, base_name="code")
router.register(r"register", RegisterViewSet, base_name="register")
router.register(r"user_detail", UserDetailViewSet, base_name="user_detail")

urlpatterns = [

    re_path("^", include(router.urls)),

]