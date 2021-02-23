# Generated by Django 3.1.1 on 2020-12-30 04:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('standardtime', '0014_auto_20201222_0715'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(choices=[('石榴庄', '石榴庄'), ('test12', 'test12'), ('国有土地出让合同办理流程', '国有土地出让合同办理流程')], max_length=255, verbose_name='项目名称')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(choices=[('石榴庄', '石榴庄'), ('test12', 'test12'), ('国有土地出让合同办理流程', '国有土地出让合同办理流程')], max_length=255, verbose_name='项目名称')),
                ('cert_name', models.CharField(choices=[('获取《一般缴款书》', '获取《一般缴款书》'), ('联系银行缴款', '联系银行缴款'), ('与经办人沟通', '与经办人沟通'), ('送审', '送审'), ('内部会商', '内部会商'), ('土地中标', '土地中标'), ('公司证照', '公司证照'), ('公司证照', '公司证照'), ('一级开发补偿费', '一级开发补偿费'), ('一级开发补偿费', '一级开发补偿费'), ('土地出让合同', '土地出让合同'), ('土地出让合同', '土地出让合同'), ('补充协议（主体变更）', '补充协议（主体变更）'), ('不动产权证（地上）', '不动产权证（地上）'), ('不动产权证（地上）', '不动产权证（地上）'), ('不动产权证（地上）', '不动产权证（地上）'), ('不动产权证（地上）', '不动产权证（地上）'), ('收地', '收地'), ('收地', '收地'), ('抵押及他证', '抵押及他证'), ('施工证', '施工证'), ('施工证', '施工证'), ('立项手续', '立项手续'), ('多规合一会商意见', '多规合一会商意见'), ('建规证', '建规证'), ('建规证', '建规证'), ('预售证', '预售证')], max_length=255, verbose_name='证书名称')),
                ('get_date', models.DateField(verbose_name='获取时间')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '项目取得证照',
                'verbose_name_plural': '项目取得证照',
                'ordering': ('id',),
                'unique_together': {('project_title', 'cert_name')},
            },
        ),
    ]
