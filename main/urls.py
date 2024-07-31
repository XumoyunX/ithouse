from django.urls import path
from main.views import *

app_name = "main"

urlpatterns = [
    path("", index, name="index"),
    path("login_course/", login_course, name="login_course"),
    path("course/", course, name="course"),
    path("new_details/<int:id>/", new_details, name="new_details"),
    path("news/", news, name="news"),
    path("course_details/<int:id>/", course_details, name="course_details"),
    path("project/<int:id>/", project, name="project")
]