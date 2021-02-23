from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid, os
from django.shortcuts import render, reverse, redirect


# Create your models here.
class District(models.Model):
	class Meta:
		verbose_name = '地区'
		verbose_name_plural = '地区'
		ordering = ('id',)

	"""docstring for ProjectDetail"""
	district = models.CharField('请输入地区名称', max_length=200, db_index=True, unique=True)
	create_date = models.DateTimeField('创建时间', default=timezone.now)
	update_date = models.DateTimeField('更新时间', default=timezone.now)
	def __str__(self):
		return self.district

def get_district_list():
	return District.objects.values_list("district", "district")

class InvStandardtime(models.Model):
	class Meta:
		verbose_name = '项目标准工期' #页面标题
		verbose_name_plural = '项目标准工期' #导航栏标题
		ordering = ('phase_text', 'index',)
		unique_together = ('cert_name', 'isSocial', 'district')
			
	"""docstring for precondition"""
	phase_text = models.CharField('阶段', max_length=200)
	index = models.IntegerField('序号')
	name_text = models.CharField('事项', max_length=200)
	cert_name = models.CharField('取得成绩（证照）', max_length = 200)
	content_text = models.CharField('具体工作', max_length=200)
	node_text = models.CharField('节点', max_length=200)
	time = models.IntegerField('单项时长')
	time_to_begin = models.IntegerField('总时长')
	dock_apartment_txt = models.CharField('责任部门', max_length=200)
	description = models.CharField('要求/注意事项/备注', max_length=200)
	isSocial = models.BooleanField('是否社会投资')
	district = models.CharField('地区', null=True, default = '公共', max_length=200)
	create_date = models.DateTimeField('创建时间', default=timezone.now)
	update_date = models.DateTimeField('更新时间', default=timezone.now)
	
	def __init__(self, *args, **kwargs):
		super(InvStandardtime, self).__init__(*args, **kwargs)
		self._meta.get_field('district').choices = get_district_list()

	def __str__(self):
		return self.content_text

def get_cert_list():
	return InvStandardtime.objects.values_list("cert_name", "cert_name")

# def get_第三天_list():
# 	return InvStandardtime.objects.values_list("cert_name", "cert_name")

class ProjectDetail(models.Model):
	class Meta:
		verbose_name = '项目'
		verbose_name_plural = '项目'
		ordering = ('id',)

	"""docstring for ProjectDetail"""
	title = models.CharField('项目名称', max_length=200, db_index=True, unique=True)
	district = models.CharField('地区', max_length=200, null=True, default = '公共')
	isSocial = models.BooleanField('是否社会投资')
	pub_date = models.DateField('拿地时间，格式为 YYYY/MM/DD', null = True)
	area_on_floor = models.PositiveIntegerField('地上建筑规模', null=True)
	district_creteria = models.CharField('使用地区标准', max_length=200, null=True, default = '公共')
	create_date = models.DateTimeField('创建时间', default=timezone.now)
	update_date = models.DateTimeField('更新时间', default=timezone.now)
	
	def __init__(self, *args, **kwargs):
		super(ProjectDetail, self).__init__(*args, **kwargs)
		self._meta.get_field('district').choices = get_district_list()
		self._meta.get_field('district_creteria').choices = get_district_list()

	def __str__(self):
		return self.title

def get_project_list():
	return ProjectDetail.objects.values_list("title", "title")

class ProjectCert(models.Model):
	class Meta:
		verbose_name = '项目取得证照'
		verbose_name_plural = '项目取得证照'
		ordering = ('id',)
		unique_together = ('project_title', 'cert_name',)

	"""docstring for ProjectDetail"""
	#select from other database
	project_title = models.CharField(max_length=255, verbose_name="项目名称", choices=get_project_list())

	#select from other database
	cert_name = models.CharField(max_length=255, verbose_name="证书名称", choices=get_cert_list())
	get_date = models.DateField('获取时间')
	description = models.CharField('备注', max_length=200, null=True, blank=True)
	create_date = models.DateTimeField('创建时间', default=timezone.now)
	update_date = models.DateTimeField('更新时间', default=timezone.now)
	
	def __init__(self, *args, **kwargs):
		super(ProjectCert, self).__init__(*args, **kwargs)
		self._meta.get_field('project_title').choices = get_project_list()
		self._meta.get_field('cert_name').choices = get_cert_list()

	def __str__(self):
		return self.project_title + self.cert_name

class Holiday(models.Model):
	class Meta:
		verbose_name = '假期时间'
		verbose_name_plural = '假期时间'
		ordering = ('begin_date',)
		unique_together = ('title', 'begin_date',)

	"""docstring for Holiday"""
	TITLES_CHOICES = (
		('y', '元旦节'),
		('c', '春节'),
		('q', '清明节'),
		('l', '劳动节'),
		('d', '端午节'),
		('z', '中秋节'),
		('g', '国庆节'),
		)
	title = models.CharField('假期名称', max_length=10, choices=TITLES_CHOICES, default='y')
	begin_date = models.DateField('开始时间')
	end_date = models.DateField('结束时间')
	days = models.IntegerField('天数')
	def __str__(self):
		return self.title + self.begin_date.strftime("%Y")

class MyModel(models.Model):
  project = models.CharField(max_length=255, verbose_name="项目名称", choices=get_project_list())
  def __init__(self, *args, **kwargs):
  	super(MyModel, self).__init__(*args, **kwargs)
  	self._meta.get_field('project').choices = get_project_list()
