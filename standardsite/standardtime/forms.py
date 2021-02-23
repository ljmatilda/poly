from django.shortcuts import render 
from .models import ProjectDetail,MyModel,ProjectCert
from django.template import loader
from django import forms


class ProjectForm(forms.ModelForm):
	"""docstring for ProjectFmodels"""
	class Meta:
		model = ProjectDetail
		fields = ['title','isSocial', 'pub_date', 'area_on_floor']

	# def __init__(self, *args, **kwargs):
	# 	user = kwargs.pop('user', None)
	# 	super(ProjectDetail, self).__init__(*args, **kwargs)
	
	exclude = ()


class ProjectCertCreateForm(forms.ModelForm):
	"""docstring for ProjectFmodels"""
	class Meta:
		model = ProjectCert
		fields = ['project_title','cert_name', 'get_date']

	def __init__(self, *args, **kwargs):
		super(ProjectCertCreateForm, self).__init__(*args, **kwargs)
		self.fields['project_title'].choices = ProjectDetail.objects.values_list("title", "title")
	
	# exclude = ()

# def get_

class ProjectSelectForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ProjectSelectForm, self).__init__(*args, **kwargs)
		self.fields['project'].choices = ProjectDetail.objects.values_list("title", "title")

	class Meta:
		model = MyModel
		fields = ['project']