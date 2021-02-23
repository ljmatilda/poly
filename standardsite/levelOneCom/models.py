from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid, os

# Create your models here.
class LevelOneComPreCon(models.Model):
	class Meta:
		verbose_name = '前置条件'
		verbose_name_plural = '前置条件'
		ordering = ('id',)
			
	"""docstring for precondition"""
	item_text = models.CharField('事项', max_length=200)
	content_text = models.CharField('工作内容', max_length=200)
	dock_apartment_txt = models.CharField('对接部门', max_length=200)
	time_text = models.IntegerField('节点时长')
	time_to_begin_text = models.IntegerField('拿地后时长')
	description = models.CharField('要求/注意事项/备注', max_length=200)
	create_date = models.DateTimeField('创建时间', default=timezone.now)
	update_date = models.DateTimeField('更新时间', default=timezone.now)
	def __str__(self):
		return self.content_text

class LevelOneComDocument(models.Model):
	class Meta:
		verbose_name = '所需资料'
		verbose_name_plural = '所需资料'
		ordering = ('id',)

	name_text = models.CharField('文件名称', max_length=200)
	dock_apartment_txt = models.CharField('对接部门', max_length=200)
	file = models.FileField('模版', blank=True, upload_to='media/presell/')
	description = models.CharField('要求/注意事项/备注', max_length=200, default='/')

	create_date = models.DateTimeField('创建时间', default=timezone.now)
	update_date = models.DateTimeField('更新时间', default=timezone.now)
	def __str__(self):
		return self.name_text
