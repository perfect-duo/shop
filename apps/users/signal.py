from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from random import randint

User = get_user_model()

# 产生随机字符串
def Random():
    user_code = []
    for i in range(0, 10):
        user_code.append(str(randint(0, 9)))
    user = ''.join(user_code)
    return user


@receiver(post_save, sender=User)
def create_user(sender, instance=None, created=False, **kwargs):
    if created:
        password = instance.password
        instance.set_password(password)
        user = Random()
        while User.objects.filter(username=user):
            user = Random()
        instance.username = user
        instance.save()


