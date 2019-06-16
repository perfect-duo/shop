from django.db import models
from datetime import datetime
from django.shortcuts import reverse
# Create your models here.


class GoodsCategory(models.Model):
    CATEGORY = (
        ('1', "一级目录"),
        ('2', "二级目录"),
        ('3', "三级目录"),
    )
    name = models.CharField(max_length=50, default=" ", verbose_name="类别名", help_text="类别名")
    code = models.CharField(max_length=50, default=" ", verbose_name="类别code", help_text="类别code")
    desc = models.TextField(default='', verbose_name='类别描述', help_text='类别描述')
    category_type = models.CharField(choices=CATEGORY, max_length=2, verbose_name='类目级别', help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父级目录", related_name="sub_cut", on_delete=models.CASCADE)
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsBrand(models.Model):
    goods_category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, verbose_name="商品类型", help_text="商品类型", related_name="goods_band", default="")
    name = models.CharField(max_length=30, default='', verbose_name="品牌名", help_text="品牌名")
    desc = models.TextField(default='', verbose_name="品牌描述", help_text="品牌描述")
    image = models.ImageField(max_length=200, upload_to="goodsbrand/", default='goodsbrand/default.jpg', blank=True, verbose_name="品牌图像")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    goods_category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, related_name="goods", verbose_name="商品类别")
    goods_number = models.CharField(max_length=50, null=True, blank=True, unique=True, verbose_name="商品号")
    name = models.CharField(max_length=100, verbose_name="商品名")
    click_num = models.IntegerField(default=0, verbose_name="点击量")
    sold_num = models.IntegerField(default=0, verbose_name="销售量")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    goods_num = models.IntegerField(default=0, verbose_name="库存数")
    market_price = models.FloatField(default=0, verbose_name="市场价格/原价")
    shop_price = models.FloatField(default=0, verbose_name="现价/销售价")
    goods_brief = models.TextField(max_length=300, default="", verbose_name="商品简述")
    goods_desc = models.TextField(max_length=800, default="", verbose_name="商品具体情况")
    transportation_price = models.FloatField(default=0, verbose_name="运费")
    goods_front_images = models.ImageField(max_length=200, upload_to="goods_front/", blank=True, verbose_name="商品正面显示图")
    is_new = models.BooleanField(default=False, verbose_name="是否新品")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class GoodImages(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品", related_name="different_images")
    images = models.ImageField(upload_to='goods/', max_length=200, blank=True, verbose_name="商品图像")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class GoodsBanner(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品")
    images = models.ImageField(upload_to="banner/", max_length=200, blank=True, verbose_name="商品轮播图")
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name








