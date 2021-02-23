# Generated by Django 3.1.1 on 2020-10-20 03:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LevelOneComDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=200, verbose_name='文件名称')),
                ('dock_apartment_txt', models.CharField(max_length=200, verbose_name='对接部门')),
                ('file', models.FileField(blank=True, upload_to='media/presell/', verbose_name='模版')),
                ('description', models.CharField(default='/', max_length=200, verbose_name='要求/注意事项/备注')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '所需资料',
                'verbose_name_plural': '所需资料',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='LevelOneComPreCon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_text', models.CharField(max_length=200, verbose_name='事项')),
                ('content_text', models.CharField(max_length=200, verbose_name='工作内容')),
                ('dock_apartment_txt', models.CharField(max_length=200, verbose_name='对接部门')),
                ('time_text', models.IntegerField(verbose_name='节点时长')),
                ('time_to_begin_text', models.IntegerField(verbose_name='拿地后时长')),
                ('description', models.CharField(max_length=200, verbose_name='要求/注意事项/备注')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '前置条件',
                'verbose_name_plural': '前置条件',
                'ordering': ('id',),
            },
        ),
    ]
