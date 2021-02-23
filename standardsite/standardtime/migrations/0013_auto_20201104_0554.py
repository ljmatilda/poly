# Generated by Django 3.1.1 on 2020-11-04 05:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('standardtime', '0012_auto_20201104_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdetail',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='projectdetail',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
    ]
