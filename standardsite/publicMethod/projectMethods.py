
from datetime import date, timedelta
from standardtime.models import ProjectDetail

# Create your method here.
class Project():
			
	def get_project(self, request):
		project_title = request.GET.get('project')

		if (project_title is None):
			item = ProjectDetail.objects.reverse()[0]
			project_title = item.title
		else:
			item = ProjectDetail.objects.get(title = project_title)

		return item



