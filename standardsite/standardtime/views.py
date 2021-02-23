from django.shortcuts import render 
from .models import ProjectDetail,MyModel,ProjectCert
from .forms import ProjectForm, ProjectSelectForm,ProjectCertCreateForm
from django.template import loader
from django.views.generic.edit import CreateView


# Create your views here.
def onEarthCertTime(request):
	text = NotSocialInvStandardtime.objects.get(index=12)
	return render(request, 'polykfflow/begin.html', {'text': text})
	# print('----------- jing test --------------', contact_form)

# Create your views here.
class ProjectCreateView(CreateView):
	model = ProjectDetail
	form_class = ProjectForm
	template_name = 'polykfflow/projectForm.html'
        

class ProjectSelectView(CreateView):
	model = MyModel
	form_class = ProjectSelectForm
	template_name = 'polykfflow/projectSelectForm.html'

class ProjectCertCreatView(CreateView):

	def get_form_kwargs(self):
		kwargs = super(ProjectCertCreatView, self).get_form_kwargs()
		if 'initial' not in kwargs:
			kwargs['initial'] = {}
			
		title = self.request.GET.get('project')
		cert_name = self.request.GET.get('cert_name')
		return_url = self.request.GET.get('return_url')
		kwargs['initial'].update({'project_title': title})
		kwargs['initial'].update({'cert_name': cert_name})
		kwargs.update(self.kwargs)
		if (return_url is None):
			success_url = self.success_url +title
		else:
			success_url = return_url+"?project=" +title

		self.success_url = success_url
		return kwargs

	model = ProjectCert
	form_class = ProjectCertCreateForm
	template_name = 'polykfflow/projectCertCreateForm.html'
	success_url = "/polyflow/whole_process_with_time/?project="


		