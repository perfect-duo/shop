from django.db import models
from datetime import datetime
# Create your models here.
from users.models import UserProfile
from goods.models import Goods


class UserFav(models.Model):

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return self.user.username


class UserMessage(models.Model):

    MESSAGE_TYPE = (
        (1, "留言"),
        (2, "投诉"),
        (3, "询问"),
        (4, "售后"),
        (5, "求购")
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    message_type = models.IntegerField(choices=MESSAGE_TYPE, default=1, verbose_name="留言类型")
    theme = models.CharField(max_length=100, verbose_name="主题")
    message = models.TextField(max_length=500, verbose_name="留言内容")
    files = models.FileField(null=True, blank=True, upload_to="message_files/", max_length=200, verbose_name="文件")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户留言"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name


class UserAddress(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    name = models.CharField(max_length=5, verbose_name="收货人姓名")
    address = models.CharField(max_length=100, verbose_name="收货人区域")
    detail_address = models.CharField(max_length=200, verbose_name="收货人详细地址")
    mobile = models.CharField(max_length=11, verbose_name="收货人手机号")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户收货地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


