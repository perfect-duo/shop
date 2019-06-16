from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ShoppingCat
from goods.models import Goods


@receiver(post_save, sender=ShoppingCat)
def create_money(sender, instance=None, created=False, **kwargs):
    if created:
        goods_money = Goods.objects.get(pk=instance.goods.id)
        instance.money = goods_money.shop_price * instance.nums
        instance.save()