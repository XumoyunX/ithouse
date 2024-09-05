from django.shortcuts import render, redirect
from main.models import Mentor, Open_Class, New, Course, Users, Questions, Modul_Model, Projects, Video, About
# from .google_sheets import append_to_sheet
# from main.forms import YourForm




def index(request):
    mentor = Mentor.objects.all()
    open_class = Open_Class.objects.all()
    course = Course.objects.all()
    media_obj = New.objects.order_by("-id")[:3]
    about = About.objects.all()



    ctx = {
        "mentor": mentor,
        "open_class": open_class,
        "new": media_obj,
        'course': course,
        'about': about

    }
    return render(request, "main/index.html", ctx)



# def login_course(request):
#     return render(request, "main/register.html")


def course(request):
    course = Course.objects.all()
    project = Projects.objects.all()
    ctx = {
       
        'course': course,
        'project': project
    }
    return render(request, "main/courses.html", ctx)



def project(request, id):
    course = Course.objects.all()
    project = Projects.objects.filter(course_id=id)
    
    ctx = {

        'project': project,
        'course': course,
        
        
        
    }
    return render(request, "main/project.html", ctx)
    



def news(request):
    new = New.objects.all()
    new_s = New.objects.order_by("-id")[:3].all()
    course = Course.objects.all()
    ctx = {
        "new": new,
        "new_s": new_s,
        'course': course
    }
    return render(request, "main/blog.html", ctx)


def new_details(request, id):
    new = New.objects.get(id=id)
    new_s = New.objects.order_by("-id")[:4].all()
    coursee = Course.objects.all()
    
    ctx = {
        "new": new,
        "new_s": new_s,
        "coursee": coursee
    }
    
    return render(request, 'main/blog-details.html', ctx)




def course_details(request, id):
    course = Course.objects.get(id=id)
    coursee = Course.objects.all()
    questions = Questions.objects.filter(course_id=id).all()
    modul_model = Modul_Model.objects.filter(course_id=id).all()
    video = Video.objects.filter(course_id=id).all()


    ctx = {
        "course": course,
        'questions': questions,
        "modul_model": modul_model,
        'video': video,
        "coursee": coursee

    }

    return render(request, 'main/courses-details.html', ctx)




# def login_course(request):
#     model = Users()
#     form = UsersFrom(request.POST, instance=model)
#     print(request.POST)
#     if form.is_valid():
#         print("aaa")
#         form.save()
#         return redirect("main:course")
#     ctx = {
#         "form": form,
#
#     }
#     return render(request, "main/register.html", ctx)


def teacher_course(request, id):
    course = Course.objects.filter(mentor_id=id).first()
    ctx = {
        "course": course,
    }
    return render(request, 'main/courses-details.html', ctx)



def login_course(request):
    course = Course.objects.all()

    return render(request, 'main/register.html', {'course': course})



