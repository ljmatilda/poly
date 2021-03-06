# Generated by Django 3.1.1 on 2020-09-30 03:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polykfflow', '0010_auto_20200930_0235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='upload',
        ),
        migrations.AddField(
            model_name='document',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='document',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 30, 3, 46, 53, 431862, tzinfo=utc), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='document',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 30, 3, 46, 53, 431897, tzinfo=utc), verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='presellcertprecon',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 30, 3, 46, 53, 431045, tzinfo=utc), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='presellcertprecon',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 30, 3, 46, 53, 431097, tzinfo=utc), verbose_name='更新时间'),
        ),
    ]
