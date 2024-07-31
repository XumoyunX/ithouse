from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from main.models import Mentor, New, Course, Users, Open_Class, Video, Projects, Questions, Modul_Model
from .forms import MentorForm, NewForm, CourseForm, UsersForm, Open_ClassForm, VideoForm, ProjectsForm, QuestionsForm, Modul_ModelForm

def login_required_decorator(f):
    return login_required(f, login_url="client:login")

@login_required_decorator
def dashboard(request):
    b = 0
    c = 0
    d = 0
    g = 0
    user = Users.objects.all()
    
    for i in user:
        b += 1 
        if i.now == 1:
            c += 1
        elif i.now == 2:
            d += 1 
        elif i.now == 4:  
            g += 1  
               
    ctx = {
        "user": user,
        "b": b,
        "c": c,
        "d": d,
        'g': g
    }
    return render(request, 'dashboard/index.html', ctx)


def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('client:dashboard')
    return render(request, 'dashboard/login.html')


@login_required_decorator
def dashboard_logout(request):
    logout(request)
    return redirect('client:login')










@login_required_decorator
def category_list(request):
    categories = Mentor.objects.all()
    ctx = {
        'categories':categories,
        "c_active": 'active'
    }
    return render(request,'dashboard/mentor/list.html',ctx)

@login_required_decorator
def category_create(request):
    model = Mentor()
    form = MentorForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:category_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/mentor/form.html', ctx)

@login_required_decorator
def category_edit(request, pk):
    model = Mentor.objects.get(id=pk)
    form = MentorForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:category_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/mentor/form.html', ctx)

@login_required_decorator
def category_delete(request, pk):
    model = Mentor.objects.get(id=pk)
    model.delete()
    return redirect('client:category_list')





@login_required_decorator
def new_list(request):
    categories = New.objects.all()
    ctx = {
        'categories':categories,
        "c_active": 'active'
    }
    return render(request,'dashboard/new/list.html',ctx)

@login_required_decorator
def new_create(request):
    model = New()
    form = NewForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:new_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/new/form.html', ctx)

@login_required_decorator
def new_edit(request, pk):
    model = New.objects.get(id=pk)
    form = NewForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:new_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/new/form.html', ctx)

@login_required_decorator
def new_delete(request, pk):
    model = New.objects.get(id=pk)
    model.delete()
    return redirect('client:new_list')




@login_required_decorator
def course_list(request):
    course = Course.objects.all()
    ctx = {
        'course':course,
        "c_active": 'active'
    }
    return render(request,'dashboard/course/list.html',ctx)


@login_required_decorator
def course_create(request):
    model = Course()
    form = CourseForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:course_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/course/form.html', ctx)


@login_required_decorator
def course_edit(request, pk):
    model = Course.objects.get(id=pk)
    form = CourseForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:course_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/course/form.html', ctx)


@login_required_decorator
def course_delete(request, pk):
    model = Course.objects.get(id=pk)
    model.delete()
    return redirect('client:course_list')



@login_required_decorator
def miracles_list(request):
    users = Users.objects.all()
    ctx = {
        'users':users,
        "c_active": 'active'
    }
    return render(request,'dashboard/let/list.html',ctx)



@login_required_decorator
def miracles_edit(request, pk):
    model = Users.objects.get(id=pk)
    form = UsersForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:miracles_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/let/form.html', ctx)




@login_required_decorator
def openclass_list(request):
    open = Open_Class.objects.all()
    ctx = {
        'open':open,
        "c_active": 'active'
    }
    return render(request,'dashboard/open/list.html',ctx)


@login_required_decorator
def openclass_create(request):
    model = Open_Class()
    form = Open_ClassForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:openclass_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/open/form.html', ctx)


@login_required_decorator
def openclass_delete(request, pk):
    model = Open_Class.objects.get(id=pk)
    model.delete()
    return redirect('client:openclass_list')


@login_required_decorator
def openclass_edit(request, pk):
    model = Open_Class.objects.get(id=pk)
    form = Open_ClassForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:openclass_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/open/form.html', ctx)




@login_required_decorator
def project_list(request):
    open = Video.objects.all()
    ctx = {
        'open':open,
        "c_active": 'active'
    }
    return render(request,'dashboard/project/list.html',ctx)



@login_required_decorator
def video_create(request):
    model = Video()
    form = VideoForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:project_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/project/form.html', ctx)





@login_required_decorator
def video_edit(request, pk):
    model = Video.objects.get(id=pk)
    form = VideoForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:project_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/project/form.html', ctx)


@login_required_decorator
def video_delete(request, pk):
    model = Video.objects.get(id=pk)
    model.delete()
    return redirect('client:project_list')






@login_required_decorator
def video_list(request):
    portfolio = Projects.objects.all()
    ctx = {
        'portfolio': portfolio,
        "c_active": 'active'
    }
    return render(request,'dashboard/video/list.html',ctx)

@login_required_decorator
def project_create(request):
    model = Projects()
    form = ProjectsForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:video_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/video/form.html', ctx)

@login_required_decorator
def project_edit(request, pk):
    model = Projects.objects.get(id=pk)
    form = ProjectsForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:video_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/video/form.html', ctx)

@login_required_decorator
def project_delete(request, pk):
    model = Projects.objects.get(id=pk)
    model.delete()
    return redirect('client:video_list')







@login_required_decorator
def questions_list(request):
    questions = Questions.objects.all()
    ctx = {
        'questions': questions,
        "c_active": 'active'
    }
    return render(request,'dashboard/questions/list.html',ctx)

@login_required_decorator
def questions_create(request):
    model = Questions()
    form = QuestionsForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:questions_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/questions/form.html', ctx)

@login_required_decorator
def questions_edit(request, pk):
    model = Questions.objects.get(id=pk)
    form = QuestionsForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:questions_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/questions/form.html', ctx)

@login_required_decorator
def questions_delete(request, pk):
    model = Questions.objects.get(id=pk)
    model.delete()
    return redirect('client:questions_list')



@login_required_decorator
def modul_list(request):
    modul_model = Modul_Model.objects.all()
    ctx = {
        'modul_model': modul_model,
        "c_active": 'active'
    }
    return render(request,'dashboard/modul/list.html',ctx)

@login_required_decorator
def modul_create(request):
    model = Modul_Model()
    form = Modul_ModelForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:modul_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/modul/form.html', ctx)

@login_required_decorator
def modul_edit(request, pk):
    model = Modul_Model.objects.get(id=pk)
    form = Modul_ModelForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:modul_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/modul/form.html', ctx)

@login_required_decorator
def modul_delete(request, pk):
    model = Modul_Model.objects.get(id=pk)
    model.delete()
    return redirect('client:modul_list')

