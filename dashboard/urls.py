from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name = "dashboard-home"),
    path('project/<int:pk>/update/', views.project_update, name = "project-update"),

]