from django.shortcuts import render
from users.models import UserProfile, MessageCode
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from users.serializers import SmsSerializers, RegisterSerializer, UserDetailSerializer
from demo_sms_send import send_sms
from random import randint
from shop.settings import MESSAGE_SIGNATURE, TEMPLATE_CODE
from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
# Create your views here.


class CustomsBackends(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user

        except Exception as e:
            return None


class SmsUserProfile(mixins.CreateModelMixin, viewsets.GenericViewSet):

    serializer_class = SmsSerializers

    # 设置验证码
    def RandomCode(self):
        code = []
        for i in range(0, 5):
            code.append(str(randint(0, 9)))
        return ''.join(code)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data['mobile']
        params = {}
        code = self.RandomCode()
        params["code"] = code

        sms_stauts = eval(send_sms(1, mobile, MESSAGE_SIGNATURE, TEMPLATE_CODE, params))
        if sms_stauts["Code"] != "OK":
            return Response({"mobile": sms_stauts["Code"]}, status=status.HTTP_400_BAD_REQUEST)
        else:
            ms = MessageCode(mobile=mobile, code=code)
            ms.save()
            return Response({"mobile":mobile}, status=status.HTTP_200_OK)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RegisterViewSet(mixins.CreateModelMixin,  viewsets.GenericViewSet):

    """
    用户注册
    """
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        SD = serializer.data
        SD["token"] = token
        SD["username"] = user.username

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # 获取用户id， 进入个人中心


class UserDetailViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):

    # 用户个人信息
    queryset = UserProfile.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_object(self):
        return self.request.user







