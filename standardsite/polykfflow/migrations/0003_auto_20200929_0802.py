# Generated by Django 3.1.1 on 2020-09-29 08:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polykfflow', '0002_auto_20200929_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='presellcertprecon',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 8, 2, 32, 13986, tzinfo=utc), verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='presellcertprecon',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 8, 2, 32, 14024, tzinfo=utc), verbose_name='更新时间'),
        ),
    ]
