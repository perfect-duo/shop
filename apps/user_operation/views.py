from django.shortcuts import render
from .models import UserFav, UserMessage, UserAddress
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, viewsets
from .serializers import UserFavSerializers, UserFavDetailSerializer, UserMessageSerializer, UserAddressSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from utils.permissions import IsOwnerOrReadOnly
# Create your views here.


class UserFavViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):

    """
    用户收藏
    list:
        用户个人中心查看收藏
    create:
        用户收藏
    delete:
        用户取消收藏
    """
    # queryset = UserFav.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    # serializer_class = UserFavSerializers
    lookup_field = "goods_id"

    def get_serializer_class(self):
        if self.action == "list":
            return UserFavDetailSerializer
        elif self.action == "create":
            return UserFavSerializers
        else:
            return UserFavSerializers

    def get_queryset(self):

        return UserFav.objects.filter(user=self.request.user)


class UserMessageViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin,
                            mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    """
    用户留言
    list:
        用户留言列表
    create:
        用户创建留言
    delete:
        用户删除留言
    retrieve:
        用户留言详情
    """
    # queryset = UserMessage.objects.all()
    serializer_class = UserMessageSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        return UserMessage.objects.filter(user=self.request.user)


class UserAddressViewSet(viewsets.ModelViewSet):

    """
    list:
        显示收货地址列表
    create:
        增加收获地址
    update:
        修改收获地址
    delete:
        删除收获地址

    """

    serializer_class = UserAddressSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)

