from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(default=datetime.now, null=True, blank=True, verbose_name="生日")
    mobile = models.CharField(null=True, blank=True, unique=True, max_length=11, verbose_name='手机号')
    gender = models.CharField(choices=(("man", "男"), ("woman", '女')), default='man', max_length=5, verbose_name='性别')

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class MessageCode(models.Model):
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    code = models.CharField(max_length=10, verbose_name="手机验证码")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "手机验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.mobile