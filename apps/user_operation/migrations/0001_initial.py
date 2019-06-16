# Generated by Django 2.0.7 on 2018-09-10 11:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='收货人姓名')),
                ('address', models.CharField(max_length=100, verbose_name='收货人区域')),
                ('detail_address', models.CharField(max_length=200, verbose_name='收货人详细地址')),
                ('mobile', models.CharField(max_length=11, verbose_name='收货人手机号')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户收货地址',
                'verbose_name_plural': '用户收货地址',
            },
        ),
        migrations.CreateModel(
            name='UserFav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户收藏',
                'verbose_name_plural': '用户收藏',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type', models.IntegerField(choices=[(1, '留言'), (2, '投诉'), (3, '询问'), (4, '售后'), (5, '求购')], default=1, verbose_name='留言类型')),
                ('theme', models.CharField(max_length=100, verbose_name='主题')),
                ('message', models.TextField(max_length=500, verbose_name='留言内容')),
                ('files', models.FileField(max_length=200, upload_to='message_files/', verbose_name='文件')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户留言',
                'verbose_name_plural': '用户留言',
            },
        ),
    ]
