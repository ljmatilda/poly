from standardtime.models import InvStandardtime, ProjectDetail, ProjectCert
from datetime import date, timedelta
from publicMethod.calTime import CalTime

# Create your views here.
calTime = CalTime()
black = "#323232"
# white = "#ffffff"
red = "#ff0000"
green = "#009900"

class ProjectCertDetail():

	plan_date = '尚未获取'
	get_date = '尚未获取'
	display_color = black
	display_text = 'yes'
	display_link = 'none'
	description = '按时获取'
	link = ''

	def __init__(self, index, phase_text, projectDetail, return_path):

		if (phase_text == '施工证阶段' or phase_text == '预售证阶段'):
			plan_item = InvStandardtime.objects.get(index=index, phase_text=phase_text, isSocial = projectDetail.isSocial)
		else:
			plan_item = InvStandardtime.objects.get(index=index, phase_text=phase_text)

		plan_date = calTime.calEndDay(projectDetail.pub_date, plan_item.time_to_begin)
		get_item = ProjectCert.objects.filter(project_title=projectDetail.title, cert_name=plan_item.cert_name)
		if (len(get_item) > 0 ):
			get_item = get_item[0]
			com = get_item.get_date - plan_date
			self.get_date = get_item.get_date.strftime("%Y.%m.%d")
		else:
			com = date.today() - plan_date

		com = com.days

		self.plan_date = plan_date.strftime("%Y.%m.%d")
		self.display_color = green if com < 0 else black if com == 0 else red
		if (self.get_date == '尚未获取' and self.display_color == green):
			self.display_color = black

		if (self.get_date == '尚未获取'):
			self.display_text = 'none'
			self.display_link = 'yes'
			self.link = '/standardtime/project/cert/create/?project='+projectDetail.title+'&&cert_name='+plan_item.cert_name + '&&return_url='+return_path

			if(com > 0):
				self.get_date = '已延迟'+str(com)+'天'

		elif (com != 0):
			if (com > 0 ):
				self.description = '延迟' + str(com) + '天'
			else:
				self.description = '提前' + str(com) + '天'

	def __str__(self):
		return 'plan_date: '+self.plan_date+', get_date: '+self.get_date+', display_color: '+self.display_color
		