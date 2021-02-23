# Generated by Django 3.1.1 on 2020-11-04 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standardtime', '0010_auto_20201103_0743'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invstandardtime',
            options={'ordering': ('phase_text', 'index'), 'verbose_name': '项目标准工期', 'verbose_name_plural': '项目标准工期'},
        ),
        migrations.AddField(
            model_name='projectdetail',
            name='isSocial',
            field=models.BooleanField(default=True, verbose_name='是否社会投资'),
        ),
    ]