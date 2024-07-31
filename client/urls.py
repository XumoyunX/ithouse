from django.urls import path
from client import views


app_name = "client"

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),
    
    path('category_list/', views.category_list, name="category_list"),
    path('category_create/', views.category_create, name="category_create"),
    path('<int:pk>/category_edit/', views.category_edit, name="category_edit"),
    path('<int:pk>/category_delete/', views.category_delete, name="category_delete"),
    
    
    path('new_list/', views.new_list, name="new_list"),
    path('new_create/', views.new_create, name="new_create"),
    path('<int:pk>/new_edit/', views.new_edit, name="new_edit"),
    path('<int:pk>/new_delete/', views.new_delete, name="new_delete"),
    
    
    path('course_list/', views.course_list, name="course_list"),
    path('course_create/', views.course_create, name="course_create"),
    path('<int:pk>/course_edit/', views.course_edit, name="course_edit"),
    path('<int:pk>/course_delete/', views.course_delete, name="course_delete"),
    
    
    path('miracles_list/', views.miracles_list, name="miracles_list"),
    path('<int:pk>/miracles_edit/', views.miracles_edit, name="miracles_edit"),
    



    path('openclass_list/', views.openclass_list, name="openclass_list"),
    path('openclass_create/', views.openclass_create, name="openclass_create"),
    path('<int:pk>/openclass_edit/', views.openclass_edit, name="openclass_edit"),
    path('<int:pk>/openclass_delete/', views.openclass_delete, name="openclass_delete"),
    
    
    path('project_list/', views.project_list, name="project_list"),
    path('video_create/', views.video_create, name="video_create"),
    path('<int:pk>/video_edit/', views.video_edit, name="video_edit"),
    path('<int:pk>/video_delete/', views.video_delete, name="video_delete"),
    
    path('video_list/', views.video_list, name="video_list"),
    path('project_create/', views.project_create, name="project_create"),
    path('<int:pk>/project_edit/', views.project_edit, name="project_edit"),
    path('<int:pk>/project_delete/', views.project_delete, name="project_delete"),
    
    path('questions_list/', views.questions_list, name="questions_list"),
    path('questions_create/', views.questions_create, name="questions_create"),
    path('<int:pk>/questions_edit/', views.questions_edit, name="questions_edit"),
    path('<int:pk>/questions_delete/', views.questions_delete, name="questions_delete"),

    path('modul_list/', views.modul_list, name="modul_list"),
    path('modul_create/', views.modul_create, name="modul_create"),
    path('<int:pk>/modul_edit/', views.modul_edit, name="modul_edit"),
    path('<int:pk>/modul_delete/', views.modul_delete, name="modul_delete"),


]