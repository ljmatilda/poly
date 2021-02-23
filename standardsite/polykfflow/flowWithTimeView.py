from django.shortcuts import render
from publicMethod.projectMethods import Project
from publicMethod.projectCertDetail import ProjectCertDetail
from publicMethod.flowTimeList import FlowTimeList

# Create your views here.
def projectApprovalFlow(request):
	project = Project()
	flowTimeList = FlowTimeList()

	item = project.get_project(request)
	path = request.path
	
	item_planBasicData = ProjectCertDetail(1, '立项阶段', item, path)
	item_planReport = ProjectCertDetail(2, '立项阶段', item, path)
	item_districtAudit = ProjectCertDetail(3, '立项阶段', item, path)
	item_cityDevAudit = ProjectCertDetail(4, '立项阶段', item, path)
	item_citycon = ProjectCertDetail(5, '立项阶段', item, path)

	item_supAgree = ProjectCertDetail(8, '地上国土手续', item, path)
	if '延迟' in item_supAgree.get_date:
		item_supAgree.get_date = '尚未取得，'+item_supAgree.get_date

	# date_pair = [[item.pub_date.strftime("%Y.%m.%d"), item_planBasicData.get_date]]
	# periods = flowTimeList.getTimeList(date_pair)

	if(item.area_on_floor > 100000):
		return render(request, 'polykfflow/withTime/projectApprovalFlow.html'
			, {
			'item': item,
			'project_title': item.title,
			'date_pub': item.pub_date.strftime("%Y.%m.%d"), 
			'isSocial': '是' if item.isSocial else '否',
			'item_planBasicData': item_planBasicData,
			'item_planReport':item_planReport,
			'item_districtAudit':item_districtAudit, 
			'item_cityDevAudit':item_cityDevAudit, 
			'item_citycon':item_citycon,
			'item_supAgree':item_supAgree,
			}
			)
	else:
		return render(request, 'polykfflow/withTime/projectApprovalLessFlow.html'
			, {
			'item': item,
			'project_title': item.title,
			'date_pub': item.pub_date.strftime("%Y.%m.%d"), 
			'isSocial': '是' if item.isSocial else '否',
			'item_planBasicData': item_planBasicData,
			'item_planReport':item_planReport,
			'item_districtAudit':item_districtAudit, 
			'item_supAgree':item_supAgree,
			}
			)

def planningPermitFlow(request):
	project = Project()
	flowTimeList = FlowTimeList()

	item = project.get_project(request)
	path = request.path

	planPeroid = '规证阶段'
	
	item1 = ProjectCertDetail(1, planPeroid, item, path)
	item2 = ProjectCertDetail(2, planPeroid, item, path)
	item3 = ProjectCertDetail(3, planPeroid, item, path)
	item4 = ProjectCertDetail(4, planPeroid, item, path)
	item5 = ProjectCertDetail(5, planPeroid, item, path)
	item6 = ProjectCertDetail(6, planPeroid, item, path)
	item7 = ProjectCertDetail(7, planPeroid, item, path)
	item8 = ProjectCertDetail(8, planPeroid, item, path)
	item9 = ProjectCertDetail(9, planPeroid, item, path)
	item10 = ProjectCertDetail(10, planPeroid, item, path)
	item11 = ProjectCertDetail(11, planPeroid, item, path)
	item12 = ProjectCertDetail(12, planPeroid, item, path)
	item121 = ProjectCertDetail(121, planPeroid, item, path)
	item13 = ProjectCertDetail(13, planPeroid, item, path)
	item14 = ProjectCertDetail(14, planPeroid, item, path)

	
	return render(request, 'polykfflow/withTime/planningPermitFlow.html'
		, {
		'item': item,
		'project_title': item.title,
		'date_pub': item.pub_date.strftime("%Y.%m.%d"), 
		'isSocial': '是' if item.isSocial else '否',
		'item_divide': item1,
		'item_basic':item2,
		'item_plan':item3, 
		'item_facility':item4, 
		'item_doc':item5,
		'item_meeting':item6,
		'item_revise':item7,
		'item_meeting2':item8,
		'item_opt':item9,
		'item_push':item10,
		'item_opinion':item11,
		'item_graph':item12,
		'item_plan_permit':item13,
		'item_plan_permit_temp':item14,
		'item_begin_graph':item121,
		}
		)

def statePropertyUnderFFlow(request):
	project = Project()
	flowTimeList = FlowTimeList()

	item = project.get_project(request)
	path = request.path

	planPeroid = '地下国土手续'
	
	item1 = ProjectCertDetail(1, planPeroid, item, path)
	item2 = ProjectCertDetail(2, planPeroid, item, path)
	item3 = ProjectCertDetail(3, planPeroid, item, path)
	item4 = ProjectCertDetail(4, planPeroid, item, path)
	item5 = ProjectCertDetail(5, planPeroid, item, path)
	item6 = ProjectCertDetail(6, planPeroid, item, path)

	item_multi_plan = ProjectCertDetail(11, '规证阶段', item, path)

	
	return render(request, 'polykfflow/withTime/statePropertyUnderFFlow.html'
		, {
		'item': item,
		'project_title': item.title,
		'date_pub': item.pub_date.strftime("%Y.%m.%d"), 
		'isSocial': '是' if item.isSocial else '否',
		'item_multi_plan': item_multi_plan,
		'item_under_sup_agree':item1,
		'item_fee':item2,
		'item_tax':item3, 
		'item_push':item4, 
		'item_cert':item5,
		'item_mortgage':item6,
		}
		)

def statePropertyOnFFlow(request):
	project = Project()
	flowTimeList = FlowTimeList()

	item = project.get_project(request)
	path = request.path

	planPeroid = '地上国土手续'
	
	item1 = ProjectCertDetail(1, planPeroid, item, path)
	item3 = ProjectCertDetail(3, planPeroid, item, path)
	item5 = ProjectCertDetail(5, planPeroid, item, path)
	item6 = ProjectCertDetail(6, planPeroid, item, path)
	item7 = ProjectCertDetail(7, planPeroid, item, path)
	item8 = ProjectCertDetail(8, planPeroid, item, path)
	item12 = ProjectCertDetail(12, planPeroid, item, path)
	item14 = ProjectCertDetail(14, planPeroid, item, path)
	
	return render(request, 'polykfflow/withTime/statePropertyOnFFlow.html'
		, {
		'item': item,
		'project_title': item.title,
		'date_pub': item.pub_date.strftime("%Y.%m.%d"), 
		'isSocial': '是' if item.isSocial else '否',
		'item_confirm': item1,
		'item_company':item3,
		'item_dev_fee':item5,
		'item_contract':item6, 
		'item_sell_fee':item7, 
		'item_supAgree':item8,
		'item_cert':item12,
		'item_get_land':item14,
		}
		)

def preSellFlow(request):
	project = Project()
	flowTimeList = FlowTimeList()

	item = project.get_project(request)
	path = request.path

	planPeroid = '预售证阶段'
	
	item1 = ProjectCertDetail(1, planPeroid, item, path)
	item2 = ProjectCertDetail(2, planPeroid, item, path)
	item3 = ProjectCertDetail(3, planPeroid, item, path)
	item4 = ProjectCertDetail(4, planPeroid, item, path)
	item5 = ProjectCertDetail(5, planPeroid, item, path)
	item6 = ProjectCertDetail(6, planPeroid, item, path)
	item7 = ProjectCertDetail(7, planPeroid, item, path)
	item8 = ProjectCertDetail(8, planPeroid, item, path)
	item9 = ProjectCertDetail(9, planPeroid, item, path)
	item10 = ProjectCertDetail(10, planPeroid, item, path)
	item11 = ProjectCertDetail(11, planPeroid, item, path)
	item12 = ProjectCertDetail(12, planPeroid, item, path)
	item13 = ProjectCertDetail(13, planPeroid, item, path)

	item_multi_plan = ProjectCertDetail(11, '规证阶段', item, path)
	item_plan_permit = ProjectCertDetail(13, '规证阶段', item, path)
	item_work = ProjectCertDetail(1, '施工证阶段', item, path)


	if(item.isSocial):
		return render(request, 'polykfflow/withTime/preSellSocialFlow.html'
			, {
			'item': item,
			'project_title': item.title,
			'date_pub': item.pub_date.strftime("%Y.%m.%d"), 
			'isSocial': '是' if item.isSocial else '否',
			'item_multi_plan': item_multi_plan,
			'item_plan_permit':item_plan_permit,
			'item_facility':item1, 
			'item_facility_fee':item2, 
			'item_name':item3, 
			'item_opinion':item4, 
			'item_tenement':item6,
			'item_work':item_work,
			'item_facility_confirm':item7,
			'item_pre_measure':item8,
			'item_first_review':item11,
			'item_sec_review':item12,
			'item_sell_cert':item13,
			}
			)
	else:
		return render(request, 'polykfflow/withTime/preSellFlow.html'
			, {
			'item': item,
			'project_title': item.title,
			'date_pub': item.pub_date.strftime("%Y.%m.%d"), 
			'isSocial': '是' if item.isSocial else '否',
			'item_multi_plan': item_multi_plan,
			'item_plan_permit':item_plan_permit,
			'item_facility':item1, 
			'item_name':item3, 
			'item_con_plan':item5,
			'item_tenement':item6,
			'item_work':item_work,
			'item_facility_confirm':item7,
			'item_first_review':item11,
			'item_sec_review':item12,
			'item_sell_cert':item13,
			}
		)
