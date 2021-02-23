from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from standardtime.models import InvStandardtime, ProjectDetail, ProjectCert
from datetime import date, timedelta
from publicMethod.calTime import CalTime
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.

def flow(request):
	# return HttpResponse("非社会投资开发流程")
	return render(request, 'polykfflow/flow2.html')

def projectSelect(request):
	return render(request, 'polykfflow/projectSelect.html')

def presellflow(request):
	return render(request, 'polykfflow/presellflow.html')

def landGrantContract(request):
	return render(request, 'polykfflow/landGrantContract.html')

def grantFee(request):
	return render(request, 'polykfflow/grantFee.html')

def gytdcrht(request):
	return render(request, 'polykfflow/index.html')

def levelOneCom(request):
	return render(request, 'polykfflow/levelOneCom.html')

def contractTax(request):
	return render(request, 'polykfflow/contractTax.html')

def partyA(request):
	return render(request, 'polykfflow/partyA.html')

def company_cert(request):
	return render(request, 'polykfflow/company_cert.html')

def level_one_com_flow(request):
	return render(request, 'polykfflow/level_one_com_flow.html')

def contract_of_land_transfer_flow(request):
	return render(request, 'polykfflow/contract_of_land_transfer_flow.html')

def statePropertyOnFFlow(request):
	phaseText = '地上国土手续'
	#土地中标
	item_bid = InvStandardtime.objects.get(index=1, phase_text=phaseText)
	#营业执照
	item_trade_cert = InvStandardtime.objects.get(index=2, phase_text=phaseText)
	#资质证书
	item_qua_cert = InvStandardtime.objects.get(index=3, phase_text=phaseText)
	#一级开发补偿协议
	item_level_one_com_agree = InvStandardtime.objects.get(index=4, phase_text=phaseText)
	#缴纳土地开发补偿费
	item_level_one_com_fee = InvStandardtime.objects.get(index=5, phase_text=phaseText)
	#土地出让合同
	item_land_grant_con = InvStandardtime.objects.get(index=6, phase_text=phaseText)
	#缴纳土地出让金并取得发票
	item_land_tran_fee = InvStandardtime.objects.get(index=7, phase_text=phaseText)
	#补充协议（主体变更）
	item_suple_agree_alter_party = InvStandardtime.objects.get(index=8, phase_text=phaseText)
	#契税及完税证明
	item_tax_fee = InvStandardtime.objects.get(index=9, phase_text=phaseText)
	#出让金及契税证明推送至大厅窗口
	item_transfer_fee_push = InvStandardtime.objects.get(index=10, phase_text=phaseText)
	#权籍调查
	item_right_survey = InvStandardtime.objects.get(index=11, phase_text=phaseText)
	#不动产权证（地上）
	item_real_estate_warrant_on_floor = InvStandardtime.objects.get(index=12, phase_text=phaseText)
	#红线验桩、物探
	item_red_line = InvStandardtime.objects.get(index=13, phase_text=phaseText)
	#收地
	item_land_resum = InvStandardtime.objects.get(index=14, phase_text=phaseText)

	return render(request, 'polykfflow/statePropertyOnFFlow.html', {
		'item_bid': item_bid, 
		'item_trade_cert': item_trade_cert,
		'item_qua_cert': item_qua_cert,
		'item_level_one_com_agree': item_level_one_com_agree,
		'item_level_one_com_fee': item_level_one_com_fee,
		'item_land_grant_con': item_land_grant_con,
		'item_land_tran_fee': item_land_tran_fee,
		'item_suple_agree_alter_party': item_suple_agree_alter_party,
		'item_tax_fee': item_tax_fee,
		'item_transfer_fee_push': item_transfer_fee_push,
		'item_right_survey': item_right_survey,
		'item_real_estate_warrant_on_floor': item_real_estate_warrant_on_floor,
		'item_red_line':item_red_line,
		'item_land_resum':item_land_resum,
		})

def begin(request):

	item_onEeathCert = InvStandardtime.objects.get(index=12, phase_text='地上国土手续')
	item_projectCert = InvStandardtime.objects.get(index=5, phase_text='立项阶段')
	item_multiPlanCons = InvStandardtime.objects.get(index=11, phase_text='规证阶段')
	item_planCert = InvStandardtime.objects.get(index=14, phase_text='规证阶段')
	item_underEeathCert = InvStandardtime.objects.get(index=6, phase_text='地下国土手续')
	item_workCert_social = InvStandardtime.objects.get(index=1, phase_text='施工证阶段', isSocial = True)
	item_workCert_notSocial = InvStandardtime.objects.get(index=1, phase_text='施工证阶段', isSocial = False)
	item_sellCert = InvStandardtime.objects.get(index=13, phase_text='预售证阶段')

	return render(request, 'polykfflow/begin.html', {
		'item_onEeathCert': item_onEeathCert.time_to_begin, 
		'item_projectCert':item_projectCert.time_to_begin,
		'item_multiPlanCons': item_multiPlanCons.time_to_begin,
		'item_planCert':item_planCert.time_to_begin,
		'item_underEeathCert': item_underEeathCert.time_to_begin,
		'item_workCert_social':item_workCert_social.time_to_begin,
		'item_workCert_notSocial': item_workCert_notSocial.time_to_begin,
		'item_sellCert':item_sellCert.time_to_begin,
		})

def land_resumption(request):
	return render(request, 'polykfflow/land_resumption.html')

def land_resumption_with_time(request):
	return render(request, 'polykfflow/withTime/land_resumption_with_time.html')

def whole_process_with_time(request):
	calTime = CalTime()
	black = "#323232"
	red = "#ff0000"

	project_title = request.GET.get('project')

	if (project_title is None):
		item = ProjectDetail.objects.reverse()[0]
		project_title = item.title
	else:
		item = ProjectDetail.objects.get(title = project_title)

	pubDate = item.pub_date
	date_pub = pubDate.strftime("%Y.%m.%d")
	
	item_onEeathCert = InvStandardtime.objects.get(index=12, phase_text='地上国土手续')
	date_onEeathCert = calTime.calEndDay(pubDate, item_onEeathCert.time_to_begin)
	get_onEeathCert = ProjectCert.objects.get(project_title=project_title, cert_name=item_onEeathCert.content_text)
	com_onEeathCert = get_onEeathCert.get_date - date_onEeathCert	

	item_projectCert = InvStandardtime.objects.get(index=5, phase_text='立项阶段')
	date_projectCert = calTime.calEndDay(pubDate, item_projectCert.time_to_begin)
	get_projectCert = ProjectCert.objects.get(project_title=project_title, cert_name=item_projectCert.content_text)
	com_projectCert = get_projectCert.get_date - date_projectCert	

	item_planCert = InvStandardtime.objects.get(index=13, phase_text='规证阶段')
	date_planCert = calTime.calEndDay(pubDate, item_planCert.time_to_begin)
	get_planCert = ProjectCert.objects.filter(project_title=project_title, cert_name=item_planCert.content_text)
	if (len(get_planCert) > 0 ):
		get_planCert = get_planCert[0]
		com_planCert = get_planCert.get_date - date_planCert
	else:
		com_planCert = date.today() - date_planCert

	item_mulPlanCert = InvStandardtime.objects.get(index=11, phase_text='规证阶段')
	date_mulPlanCert = calTime.calEndDay(pubDate, item_mulPlanCert.time_to_begin)
	get_mulPlanCert = ProjectCert.objects.filter(project_title=project_title, cert_name=item_mulPlanCert.content_text)
	if (len(get_mulPlanCert) > 0 ):
		get_mulPlanCert = get_mulPlanCert[0]
		com_mulPlanCert = get_mulPlanCert.get_date - date_mulPlanCert
	else:
		com_mulPlanCert = date.today() - date_mulPlanCert

	item_workCert = InvStandardtime.objects.get(index=1, phase_text='施工证阶段', isSocial = item.isSocial).time_to_begin
	date_workCert = calTime.calEndDay(pubDate, item_workCert).strftime("%Y.%m.%d")

	time_underEeathCert = InvStandardtime.objects.get(index=6, phase_text='地下国土手续').time_to_begin
	date_underEeathCert = calTime.calEndDay(pubDate, time_underEeathCert).strftime("%Y.%m.%d")

	item_sellCert = InvStandardtime.objects.get(index=13, phase_text='预售证阶段').time_to_begin
	date_sellCert = calTime.calEndDay(pubDate, item_sellCert).strftime("%Y.%m.%d")

	return render(request, 'polykfflow/withTime/whole_process_with_time.html'
		, {
		'item': item,
		'project_title': project_title,
		'date_pub': date_pub, 
		'isSocial': '是' if item.isSocial else '否',
		'date_onEeathCert': date_onEeathCert.strftime("%Y.%m.%d"), 
		'date_projectCert':date_projectCert.strftime("%Y.%m.%d"), 
		'date_planCert':date_planCert.strftime("%Y.%m.%d"), 
		'date_mulPlanCert':date_mulPlanCert.strftime("%Y.%m.%d"), 
		'date_workCert':date_workCert,
		'date_underEeathCert':date_underEeathCert,
		'date_sellCert':date_sellCert,
		#begin really get time
		'get_onEeathCert': get_onEeathCert.get_date.strftime("%Y.%m.%d"),
		'color_onEeathCert': black if com_onEeathCert <= timedelta(days=0) else red,
		'get_projectCert': get_projectCert.get_date.strftime("%Y.%m.%d"),
		'color_projectCert': black if com_projectCert <= timedelta(days=0) else red,
		'get_planCert': '尚未获取' if len(get_planCert)==0 else get_planCert.get_date.strftime("%Y.%m.%d"),
		'color_planCert': black if com_planCert <= timedelta(days=0) else red,
		'get_mulPlanCert': '尚未获取' if len(get_mulPlanCert)==0 else get_mulPlanCert.get_date.strftime("%Y.%m.%d"),
		'color_mulPlanCert': black if com_mulPlanCert <= timedelta(days=0) else red,
		}
		)

def statePropertyOnFFlow_with_time(request):
	phaseText = '地上国土手续'

	calTime = CalTime()
	item = ProjectDetail.objects.reverse()[0]
	pubDate = item.pub_date
	date_pub = pubDate.strftime("%Y.%m.%d")

	#土地中标
	item_bid = InvStandardtime.objects.get(index=1, phase_text=phaseText)
	date_bid = calTime.calEndDay(pubDate, item_bid.time_to_begin).strftime("%Y.%m.%d")
	#营业执照
	item_trade_cert = InvStandardtime.objects.get(index=2, phase_text=phaseText)
	date_trade_cert = calTime.calEndDay(pubDate, item_trade_cert.time_to_begin).strftime("%Y.%m.%d")
	#资质证书
	item_qua_cert = InvStandardtime.objects.get(index=3, phase_text=phaseText)
	date_qua_cert = calTime.calEndDay(pubDate, item_qua_cert.time_to_begin).strftime("%Y.%m.%d")
	#一级开发补偿协议
	item_level_one_com_agree = InvStandardtime.objects.get(index=4, phase_text=phaseText)
	date_level_one_com_agree = calTime.calEndDay(pubDate, item_level_one_com_agree.time_to_begin).strftime("%Y.%m.%d")
	#缴纳土地开发补偿费
	item_level_one_com_fee = InvStandardtime.objects.get(index=5, phase_text=phaseText)
	date_level_one_com_fee = calTime.calEndDay(pubDate, item_level_one_com_fee.time_to_begin).strftime("%Y.%m.%d")
	#土地出让合同
	item_land_grant_con = InvStandardtime.objects.get(index=6, phase_text=phaseText)
	date_land_grant_con = calTime.calEndDay(pubDate, item_land_grant_con.time_to_begin).strftime("%Y.%m.%d")
	#缴纳土地出让金并取得发票
	item_land_tran_fee = InvStandardtime.objects.get(index=7, phase_text=phaseText)
	date_land_tran_fee = calTime.calEndDay(pubDate, item_land_tran_fee.time_to_begin).strftime("%Y.%m.%d")
	#补充协议（主体变更）
	item_suple_agree_alter_party = InvStandardtime.objects.get(index=8, phase_text=phaseText)
	date_suple_agree_alter_party = calTime.calEndDay(pubDate, item_suple_agree_alter_party.time_to_begin).strftime("%Y.%m.%d")
	#契税及完税证明
	item_tax_fee = InvStandardtime.objects.get(index=9, phase_text=phaseText)
	date_tax_fee = calTime.calEndDay(pubDate, item_tax_fee.time_to_begin).strftime("%Y.%m.%d")
	#出让金及契税证明推送至大厅窗口
	item_transfer_fee_push = InvStandardtime.objects.get(index=10, phase_text=phaseText)
	date_transfer_fee_push = calTime.calEndDay(pubDate, item_transfer_fee_push.time_to_begin).strftime("%Y.%m.%d")
	#权籍调查
	item_right_survey = InvStandardtime.objects.get(index=11, phase_text=phaseText)
	date_right_survey = calTime.calEndDay(pubDate, item_right_survey.time_to_begin).strftime("%Y.%m.%d")
	#不动产权证（地上）
	item_real_estate_warrant_on_floor = InvStandardtime.objects.get(index=12, phase_text=phaseText)
	date_real_estate_warrant_on_floor = calTime.calEndDay(pubDate, item_real_estate_warrant_on_floor.time_to_begin).strftime("%Y.%m.%d")
	#红线验桩、物探
	item_red_line = InvStandardtime.objects.get(index=13, phase_text=phaseText)
	date_red_line = calTime.calEndDay(pubDate, item_red_line.time_to_begin).strftime("%Y.%m.%d")
	#收地
	item_land_resum = InvStandardtime.objects.get(index=14, phase_text=phaseText)
	date_land_resum = calTime.calEndDay(pubDate, item_land_resum.time_to_begin).strftime("%Y.%m.%d")

	return render(request, 'polykfflow/withTime/statePropertyOnFFlow_with_time.html', {
		'item':item,
		'date_pub': date_pub,
		'isSocial': '是' if item.isSocial else '否',
		'item_bid': item_bid, 'date_bid':date_bid,
		'item_trade_cert': item_trade_cert, 'date_trade_cert': date_trade_cert,
		'item_qua_cert': item_qua_cert, 'date_qua_cert': date_qua_cert,
		'item_level_one_com_agree': item_level_one_com_agree, 'date_level_one_com_agree': date_level_one_com_agree,
		'item_level_one_com_fee': item_level_one_com_fee, 'date_level_one_com_fee': date_level_one_com_fee,
		'item_land_grant_con': item_land_grant_con, 'date_land_grant_con': date_land_grant_con,
		'item_land_tran_fee': item_land_tran_fee, 'date_land_tran_fee': date_land_tran_fee,
		'item_suple_agree_alter_party': item_suple_agree_alter_party, 'date_suple_agree_alter_party': date_suple_agree_alter_party,
		'item_tax_fee': item_tax_fee, 'date_tax_fee': date_tax_fee,
		'item_transfer_fee_push': item_transfer_fee_push, 'date_transfer_fee_push': date_transfer_fee_push,
		'item_right_survey': item_right_survey, 'date_right_survey': date_right_survey,
		'item_real_estate_warrant_on_floor': item_real_estate_warrant_on_floor, 'date_real_estate_warrant_on_floor': date_real_estate_warrant_on_floor,
		'item_red_line':item_red_line, 'date_red_line':date_red_line,
		'item_land_resum':item_land_resum, 'date_land_resum':date_land_resum,
		})

def test(request):
    item_onEeathCert = InvStandardtime.objects.get(index=12)
    print('----------- jing test --------------', item_onEeathCert)
    return render(request, 'polykfflow/test.html', {'item': item_onEeathCert})
	# return render(request, 'polykfflow/test.html')