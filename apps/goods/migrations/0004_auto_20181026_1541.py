# Generated by Django 2.0.7 on 2018-10-26 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20180913_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodimages',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='different_images', to='goods.Goods', verbose_name='商品'),
        ),
    ]
