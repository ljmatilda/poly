from django.contrib import admin

from .models import InvStandardtime, ProjectDetail, Holiday, ProjectCert, District

# Register your models here.
@admin.register(InvStandardtime)
class InvStandardtimeAdmin(admin.ModelAdmin):
	list_display = ('phase_text', 'district', 'index', 'name_text', 'cert_name','content_text','node_text', 
		'time', 'time_to_begin','dock_apartment_txt', 'isSocial', 'description')
	list_filter = ['phase_text', 'district']
	search_fields = ['phase_text', 'name_text', 'district']

@admin.register(ProjectDetail)
class ProjectDetailAdmin(admin.ModelAdmin):
	list_display = ('id','title', 'district', 'district_creteria', 'isSocial', 'pub_date', 'area_on_floor', 'create_date')

@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'begin_date', 'end_date','days')

@admin.register(ProjectCert)
class ProjectCertAdmin(admin.ModelAdmin):
	list_display = ('id', 'project_title', 'cert_name', 'get_date', 'description')
	list_filter = ['project_title']
	search_fields = ['project_title', 'cert_name']

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
	list_display = ('id', 'district')
