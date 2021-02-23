from django.urls import path
from . import views


# Create your views here.
app_name = 'standardtime'
urlpatterns = [
path('project/create/', views.ProjectCreateView.as_view(success_url="/polyflow/whole_process_with_time"), name='project_create'),
path('project/select/', views.ProjectSelectView.as_view(success_url="/polyflow/whole_process_with_time"), name='project_select'),
path('project/cert/create/', views.ProjectCertCreatView.as_view(), name='project_cert_create'),
]