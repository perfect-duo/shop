# Generated by Django 2.0.7 on 2018-11-30 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0003_auto_20181027_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessage',
            name='files',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to='message_files/', verbose_name='文件'),
        ),
    ]
