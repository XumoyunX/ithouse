from django.shortcuts import render, redirect
from main.models import Mentor, Open_Class, New, Course, Users, Questions, Modul_Model, Projects, Video
from .google_sheets import append_to_sheet
from main.forms import YourForm




def index(request):
    mentor = Mentor.objects.all()
    open_class = Open_Class.objects.all()
    course = Course.objects.all()
    media_obj = New.objects.order_by("-id")[:3]

    if media_obj:
        first_media_obj = media_obj.first()
        if first_media_obj.file.name.endswith('.mp4') or first_media_obj.file.name.endswith('.avi'):
            video_url = first_media_obj.file.url
            image_url = None
        else:
            image_url = first_media_obj.file.url
            video_url = None
    else:
        video_url = None
        image_url = None


    ctx = {
        "mentor": mentor,
        "open_class": open_class,
        "new": media_obj,
        'course': course,
        'video_url': video_url,
        'image_url': image_url
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




def login_course(request):
    if request.method == 'POST':
        form = YourForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            data = [
                [form.cleaned_data['course'].course_name, form.cleaned_data['name'], form.cleaned_data['number']]

            ]
            print(form.cleaned_data['course'], "14 qator")
            # Google Sheet ID and range (e.g., 'Sheet1!A1')
            SPREADSHEET_ID = '1TgT3iHhry8PTV2s0VwvEAsNHbNIBbNW5hXhehBudsOs'
            RANGE_NAME = 'A1'
            append_to_sheet(SPREADSHEET_ID, RANGE_NAME, data)
            # return redirect('/submit')
            return redirect("main:course")
    else:
        form = YourForm()
    return render(request, 'main/register.html', {'form': form})
