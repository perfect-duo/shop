from django.db import models
from datetime import datetime
from users.models import UserProfile
from goods.models import Goods
# Create your models here.


class ShoppingCat(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品")
    nums = models.IntegerField(default=0, verbose_name="购买数量")
    money = models.FloatField(default=0, verbose_name="金额")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}({1})".format(self.goods.name, self.nums)


# WAIT_BUYER_PAY	交易创建，等待买家付款
# TRADE_CLOSED	未付款交易超时关闭，或支付完成后全额退款
# TRADE_SUCCESS	交易支付成功
# TRADE_FINISHED	交易结束，不可退款
class OrderForm(models.Model):
    PAY_STATUS = (
        ('TRADE_SUCCESS', "交易支付成功"),
        ("TRADE_CLOSED", "未付款交易超时关闭，或支付完成后全额退款"),
        ("WAIT_BUYER_PAY", "交易创建，等待买家付款"),
        ("TRADE_FINISHED", "交易结束，不可退款")
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    # shop_cat = models.ForeignKey(ShoppingCat, on_delete=models.CASCADE, verbose_name="购物车")
    order_no = models.CharField(max_length=200, unique=True, verbose_name="订单编号")
    trade_no = models.CharField(max_length=200, verbose_name="第三方编号")
    pay_status = models.CharField(max_length=30, choices=PAY_STATUS, default="WAIT_BUYER_PAY", verbose_name="支付状态")
    post_script = models.TextField(max_length=400, verbose_name="留言")
    order_mount = models.FloatField(default=0, verbose_name="订单金额")
    pay_time = models.DateTimeField(blank=True, null=True, verbose_name="支付时间")
    address = models.CharField(max_length=200, verbose_name="收货地址")
    signer_name = models.CharField(max_length=200, verbose_name="签收人")
    signer_mobile = models.CharField(max_length=11, verbose_name="签收人电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_no


class OrderGoods(models.Model):

    order_form = models.ForeignKey(OrderForm, on_delete=models.CASCADE, related_name="order_goods", verbose_name="订单")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品")
    num = models.IntegerField(default=0, verbose_name="商品数量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "订单商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name

















