from django.conf.urls import url
from . import views
from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns



router = routers.DefaultRouter()
urlpatterns = [
    path('companies/', views.CompanyList.as_view()),   # get all , post one
    path('company/companyid/<int:company_id>', views.Company_company_id_get_update_delete.as_view()),  # GUD operations
    path('users/', views.AspnetusersList.as_view()),  # get all, post one
    path('user/userid/<int:user_id>', views.Aspnetusers_get_update_delete.as_view()),    # GUD operations
    path('users/companyid/<int:company_id>', views.Aspnetusers_of_companyList.as_view()),  # get company's users
    path('users/username/<str:user_name>', views.Aspnetusers_of_username.as_view()),   # get user by user name
    path('users/roles/', views.AspnetrolesList.as_view()),  # get all roles, post one
    path('projects/', views.ProjectList.as_view()),    # get all, post one
    path('project/projectid/<int:project_id>', views.Project_project_id_get_update_delete.as_view()),  # GUD operations
    path('projects/companyid/<int:company_id>', views.Projects_of_company.as_view()),  # get projects of company
    path('documents/', views.DocumentsList.as_view()),  # get all, post one
    path('documents/project/<int:project_id>', views.Documents_of_project_List.as_view()),
    path('document/project/<int:project_id>/<int:document_id>', views.Document_with_projectid_documentid.as_view()),
    path('leads/', views.LeadsList.as_view()),
    path('join/', views.UsersJoinList.as_view()),
    path('join/test/<str:user_name>', views.Aspnetusers_join_aspnetroles.as_view()),
    path('fileupload/', views.UploadFiles.as_view()),

]


urlpatterns = format_suffix_patterns(urlpatterns)