# Generated by Django 3.1.1 on 2020-10-15 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polykfflow', '0014_auto_20201009_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='presellcertprecon',
            name='time_to_begin_text',
            field=models.IntegerField(default=1, verbose_name='拿地后时长'),
        ),
    ]