from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from standardtime.models import InvStandardtime, ProjectDetail, ProjectCert
from datetime import date, timedelta
from publicMethod.calTime import CalTime
from publicMethod.projectMethods import Project
from publicMethod.projectCertDetail import ProjectCertDetail
from django.contrib import messages
from django.shortcuts import get_object_or_404

def whole_process_with_time(request):
	
	project = Project()
	item = project.get_project(request)

	path = request.path

	item_onEeathCert = ProjectCertDetail(12, '地上国土手续', item, path)
	
	if(item.area_on_floor > 100000):
		item_projectCert = ProjectCertDetail(5, '立项阶段', item, path)
	else:
		item_projectCert = ProjectCertDetail(3, '立项阶段', item, path)

	item_planCert = ProjectCertDetail(13, '规证阶段', item, path)
	item_mulPlanCert = ProjectCertDetail(11, '规证阶段', item, path)
	item_workCert = ProjectCertDetail(1, '施工证阶段', item, path)
	time_underEeathCert = ProjectCertDetail(6, '地下国土手续', item, path)
	item_sellCert = ProjectCertDetail(13, '预售证阶段', item, path)

	return render(request, 'polykfflow/withTime/whole_process_with_time.html'
		, {
		'item': item,
		'project_title': item.title,
		'date_pub': item.pub_date.strftime("%Y.%m.%d"), 
		'isSocial': '是' if item.isSocial else '否',
		'item_onEeathCert': item_onEeathCert,
		'item_projectCert':item_projectCert,
		'item_planCert':item_planCert, 
		'item_mulPlanCert':item_mulPlanCert, 
		'item_workCert':item_workCert,
		'item_underEeathCert':time_underEeathCert,
		'item_sellCert':item_sellCert,
		}
		)

