# Generated by Django 3.1.1 on 2020-09-29 08:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polykfflow', '0003_auto_20200929_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presellcertprecon',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 8, 4, 22, 205230, tzinfo=utc), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='presellcertprecon',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 8, 4, 22, 205287, tzinfo=utc), verbose_name='更新时间'),
        ),
    ]
