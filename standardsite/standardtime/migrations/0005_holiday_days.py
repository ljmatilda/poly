# Generated by Django 3.1.1 on 2020-10-23 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standardtime', '0004_auto_20201023_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='holiday',
            name='days',
            field=models.IntegerField(default=1, verbose_name='天数'),
            preserve_default=False,
        ),
    ]
