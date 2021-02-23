# Generated by Django 3.1.1 on 2020-10-23 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standardtime', '0002_projectdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetail',
            name='pub_date',
            field=models.DateField(null=True, verbose_name='拿地时间'),
        ),
        migrations.AlterField(
            model_name='projectdetail',
            name='title',
            field=models.CharField(db_index=True, max_length=200, verbose_name='请输入项目名称'),
        ),
    ]
