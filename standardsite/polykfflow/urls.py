from django.urls import path
from . import views, withTimeViews, wholeProcessWithTimeView, flowWithTimeView


# Create your views here.
app_name = 'polykfflow'
urlpatterns = [
path('', views.begin, name = 'begin'),
path('projectSelect', views.projectSelect, name = 'projectSelect'),
path('flow/', views.flow, name = 'flow'),
path('presellflow/', views.presellflow, name = 'presellflow'),
path('gytdcrht/', views.gytdcrht, name = 'gytdcrht'),
path('landGrantContract/', views.landGrantContract, name = 'landGrantContract'),
path('grantFee/', views.grantFee, name = 'grantFee'),
path('levelOneCom/', views.levelOneCom, name = 'levelOneCom'),
path('contractTax/', views.contractTax, name = 'contractTax'),
path('partyA/', views.partyA, name = 'partyA'),
path('statePropertyOnFFlow/', views.statePropertyOnFFlow, name = 'statePropertyOnFFlow'),
path('statePropertyUnderFFlow/', views.statePropertyUnderFFlow, name = 'statePropertyUnderFFlow'),
path('projectApprovalFlow/', views.projectApprovalFlow, name = 'projectApprovalFlow'),
path('planningPermitFlow/', views.planningPermitFlow, name = 'planningPermitFlow'),
path('preSellFlow/', views.preSellFlow, name = 'preSellFlow'),

path('land_resumption/', views.land_resumption, name = 'land_resumption'),
path('company_cert/', views.company_cert, name = 'company_cert'),
path('level_one_com_flow/', views.level_one_com_flow, name = 'level_one_com_flow'),
path('contract_of_land_transfer_flow/', views.contract_of_land_transfer_flow, name = 'contract_of_land_transfer_flow'),


#with time part
path('whole_process_with_time/', wholeProcessWithTimeView.whole_process_with_time, name = 'whole_process_with_time'),
# path('statePropertyOnFFlow_with_time', views.statePropertyOnFFlow_with_time, name = 'statePropertyOnFFlow_with_time'),
path('land_resumption_with_time', views.land_resumption_with_time, name = 'land_resumption_with_time'),

#withTimeView
path('with_time/company_cert', withTimeViews.company_cert, name = 'company_cert'),
path('with_time/level_one_com_flow', withTimeViews.level_one_com_flow, name = 'level_one_com_flow'),
path('with_time/level_one_com', withTimeViews.level_one_com, name = 'level_one_com'),
path('with_time/contract_of_land_transfer_flow', withTimeViews.contract_of_land_transfer_flow, name = 'contract_of_land_transfer_flow'),
path('with_time/landGrantContract/', withTimeViews.landGrantContract, name = 'landGrantContract'),
path('with_time/projectApprovalFlow/', flowWithTimeView.projectApprovalFlow, name = 'projectApprovalFlow'),
path('with_time/planningPermitFlow/', flowWithTimeView.planningPermitFlow, name = 'planningPermitFlow'),
path('with_time/preSellFlow/', flowWithTimeView.preSellFlow, name = 'preSellFlow'),
path('with_time/statePropertyUnderFFlow/', flowWithTimeView.statePropertyUnderFFlow, name = 'statePropertyUnderFFlow'),
path('with_time/statePropertyOnFFlow/', flowWithTimeView.statePropertyOnFFlow, name = 'statePropertyOnFFlow'),

path('test/', views.test, name = 'test'),
]