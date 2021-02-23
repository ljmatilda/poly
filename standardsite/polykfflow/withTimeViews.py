from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from standardtime.models import InvStandardtime,ProjectDetail
from datetime import date, timedelta
from publicMethod.calTime import CalTime
from publicMethod.projectMethods import Project

# Create your views here.

def company_cert(request):
	phaseText = '地上国土手续'
	calTime = CalTime()
	item = ProjectDetail.objects.reverse()[0]
	pubDate = item.pub_date
	
	time_tradeCert = InvStandardtime.objects.get(index=2, phase_text=phaseText).time_to_begin	
	time_qualiCert = InvStandardtime.objects.get(index=3, phase_text=phaseText).time_to_begin

	return render(request, 'polykfflow/withTime/company_cert.html', {
		'item': item,
		'isSocial': '是' if item.isSocial else '否',
		'date_pub': pubDate.strftime("%Y.%m.%d"), 
		'date_tradeCert': calTime.getEndDay(pubDate, time_tradeCert),
		'date_qualiCert': calTime.getEndDay(pubDate, time_qualiCert),
		})

def level_one_com_flow(request):
	phaseText = '地上国土手续'
	calTime = CalTime()
	item = ProjectDetail.objects.reverse()[0]
	pubDate = item.pub_date
	
	time_levelOneComPro = InvStandardtime.objects.get(index=4, phase_text=phaseText).time_to_begin	
	time_levelOneComFee = InvStandardtime.objects.get(index=5, phase_text=phaseText).time_to_begin

	return render(request, 'polykfflow/withTime/level_one_com_flow.html', {
		'item': item,
		'isSocial': '是' if item.isSocial else '否',
		'date_pub': pubDate.strftime("%Y.%m.%d"), 
		'time_levelOneComPro': calTime.getEndDay(pubDate, time_levelOneComPro),
		'time_levelOneComFee': calTime.getEndDay(pubDate, time_levelOneComFee),
		})

def level_one_com(request):
	phaseText = '地上国土手续'
	phaseText_level_one = '一级开发补偿费阶段'
	calTime = CalTime()
	item = ProjectDetail.objects.reverse()[0]
	pubDate = item.pub_date 
	
	#成交确认书
	time_sales_conf = InvStandardtime.objects.get(index=1, phase_text=phaseText).time_to_begin	
	#一级开发补偿协议
	time_levelOneComPro = InvStandardtime.objects.get(index=4, phase_text=phaseText).time_to_begin	
	#获取一般缴款书
	time_general_letter_of_payment = InvStandardtime.objects.get(index=1, phase_text=phaseText_level_one).time_to_begin	
	#缴款完成
	time_finish_payment = InvStandardtime.objects.get(index=2, phase_text=phaseText_level_one).time_to_begin	
	#缴纳土地开发补偿费
	time_levelOneComFee = InvStandardtime.objects.get(index=5, phase_text=phaseText).time_to_begin
	#收地
	time_get_land = InvStandardtime.objects.get(index=14, phase_text=phaseText).time_to_begin	

	return render(request, 'polykfflow/withTime/levelOneCom.html', {
		'item': item,
		'isSocial': '是' if item.isSocial else '否',
		'date_pub': pubDate.strftime("%Y.%m.%d"), 
		'time_sales_conf': calTime.getEndDay(pubDate, time_sales_conf),
		'time_levelOneComPro': calTime.getEndDay(pubDate, time_levelOneComPro),
		'time_general_letter_of_payment': calTime.getEndDay(pubDate, time_general_letter_of_payment),
		'time_finish_payment': calTime.getEndDay(pubDate, time_finish_payment),
		'time_levelOneComFee': calTime.getEndDay(pubDate, time_levelOneComFee),
		'time_get_land': calTime.getEndDay(pubDate, time_get_land),
		})


def contract_of_land_transfer_flow(request):
	phaseText = '地上国土手续'
	calTime = CalTime()
	item = ProjectDetail.objects.reverse()[0]
	pubDate = item.pub_date
	
	#土地出让合同
	time_contract_of_land_transfer = InvStandardtime.objects.get(index=6, phase_text=phaseText).time_to_begin	
	#缴纳土地出让金
	time_land_grant_fee = InvStandardtime.objects.get(index=7, phase_text=phaseText).time_to_begin

	return render(request, 'polykfflow/withTime/contract_of_land_transfer_flow.html', {
		'item': item,
		'isSocial': '是' if item.isSocial else '否',
		'date_pub': pubDate.strftime("%Y.%m.%d"), 
		'time_contract_of_land_transfer': calTime.getEndDay(pubDate, time_contract_of_land_transfer),
		'time_land_grant_fee': calTime.getEndDay(pubDate, time_land_grant_fee),
		})

def landGrantContract(request):
	phaseText = '地上国土手续'
	phaseText1 = '土地出让合同'
	calTime = CalTime()
	project = Project()
	
	item = project.get_project(request)
	pubDate = item.pub_date
	
	#土地中标
	time_bid = InvStandardtime.objects.get(index=1, phase_text=phaseText).time_to_begin	
	#与经办人沟通
	time_communicate = InvStandardtime.objects.get(index=1, phase_text=phaseText1).time_to_begin
	#送审
	time_submit_for_approval = InvStandardtime.objects.get(index=2, phase_text=phaseText1).time_to_begin
	#内部会商
	time_discuss = InvStandardtime.objects.get(index=3, phase_text=phaseText1).time_to_begin
	#内部会商
	time_finish = InvStandardtime.objects.get(index=6, phase_text=phaseText).time_to_begin

	return render(request, 'polykfflow/withTime/landGrantContract.html', {
		'item': item,
		'isSocial': '是' if item.isSocial else '否',
		'date_pub': pubDate.strftime("%Y.%m.%d"), 
		'time_bid': calTime.getEndDay(pubDate, time_bid),
		'time_communicate': calTime.getEndDay(pubDate, time_communicate),
		'time_submit_for_approval': calTime.getEndDay(pubDate, time_submit_for_approval),
		'time_discuss': calTime.getEndDay(pubDate, time_discuss),
		'time_finish': calTime.getEndDay(pubDate, time_finish),
		})

