from rest_framework import serializers
from users.models import UserProfile, MessageCode
import re
from random import randint
from shop.settings import VERIFY_MOBILE
from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator


class SmsSerializers(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, data):

        # 手机号是否被注册
        mobile = UserProfile.objects.filter(mobile=data)
        if mobile:
            raise serializers.ValidationError("该手机号已经被注册")

        # 验证手机号码是否合法
        if not re.match(VERIFY_MOBILE, data):
            raise serializers.ValidationError("请输入正确的手机号格式")

        # 验证手机号码是否过期 （设置过期时间为一分钟）
        time = datetime.now() - timedelta(minutes=1)
        if MessageCode.objects.filter(mobile=data):
            if MessageCode.objects.filter(add_time__gt=time, mobile=data):
                raise serializers.ValidationError("该手机号码发送过于频繁")

        return data


class RegisterSerializer(serializers.ModelSerializer):

    code = serializers.CharField(max_length=5, min_length=5, write_only=True, label="验证码")
    password1 = serializers.CharField(min_length=8,write_only=True, label="确认密码",
                                      style={"input_type": "password"})
    password = serializers.CharField(min_length=8, write_only=True, label="输入密码",
                                     style={"input_type": "password"})
    # username = serializers.HiddenField(default=RandomCode())
    # 查找唯一型
    # username = serializers.CharField(required=True, validators=
    #                                  [UniqueValidator(queryset=UserProfile.objects.all())
    #                                 ], message="该用户已被注册")

    def validate_code(self, code):

        message_code = MessageCode.objects.filter(mobile=self.initial_data['mobile']).order_by("-add_time")
        time = datetime.now() - timedelta(minutes=5)
        if message_code:
            if message_code[0].add_time < time:
                raise serializers.ValidationError("该验证码已经失效")

            if message_code[0].code != code:
                raise serializers.ValidationError("验证码错误")
        else:
            raise serializers.ValidationError("验证码错误")

    def validate_password(self, password):

        if password != self.initial_data["password1"]:
            raise serializers.ValidationError("两次密码不一致")
        return password

    def validate(self, attrs):

        del attrs["password1"]
        del attrs["code"]
        return attrs

    # 使用随机数产生用户
    # def RandomCode(self):
    #     user_code = []
    #     for i in range(0, 10):
    #         user_code.append(str(randint(0, 9)))
    #     user = ''.join(user_code)
    #     if UserProfile.objects.filter(username=user):
    #         self.RandomCode()
    #     return user
    #
    # def create(self, validated_data):
    #     # validated_data["username"] = self.RandomCode()
    #     # validated_data["password"] = make_password(validated_data["password"])
    #     # return UserProfile.objects.create(**validated_data)
    #     user = super(RegisterSerializer, self).create(validated_data=validated_data)
    #     user.set_password(validated_data["password"])
    #     user.username = self.RandomCode()
    #     user.save()
    #     return user

    class Meta:
        model = UserProfile
        fields = ("mobile", "code", "password", "password1")


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ("username", "name", "birthday", "gender", "mobile")





