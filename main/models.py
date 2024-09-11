from django.db import models
from ckeditor.fields import RichTextField
import os




class Mentor(models.Model):
    img = models.ImageField(upload_to="images/")
    last_name = models.CharField(max_length=50)
    direction = models.CharField(max_length=50)
    text = RichTextField()
    
    def __str__(self):
        return self.last_name
    
    
    
    
class Open_Class(models.Model):
    img = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=250)
    day = models.CharField(max_length=250)
    day_time = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    text = models.TextField()
    
    def __str__(self):
        return self.name
    
    
    
class New(models.Model):
    file =  models.FileField(upload_to='uploads/%Y-%m-%d')
    name = models.TextField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    @property
    def ext(self):
        return (os.path.splitext(self.file.name)[1])[1:].lower()

    @property
    def is_image(self):
        return self.ext in ['jpg', 'jpeg', 'png', 'gif', 'webp', 'bmp']

    @property
    def is_video(self):
        return self.ext in ['mp4', 'webm', 'mpeg']

    @property
    def is_audio(self):
        return self.ext in ['mp3', 'wav']
    
    
    
class Course(models.Model):
    mentor = models.ForeignKey(Mentor, null=True, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="images/")  
    course_name = models.CharField(max_length=250)
    text = models.TextField()
    course_table = models.CharField(max_length=250)
    lesson_number = models.CharField(max_length=50)
    month = models.CharField(max_length=20)
    bonus = models.CharField(max_length=250)
    
    def __str__(self):
        return self.course_name
        
    
        
    
    
    
class Users(models.Model):
    
    YES = 1
    NO = 2
    THINKING = 3
    NOT_INTERESTING = 4
    
    
    ONLINE = 5
    OFFINE = 6   
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    number =  models.CharField(max_length=250)
    comment = models.TextField(blank=True, null=True)
    meneger = models.CharField(max_length=50, blank=True, null=True)
    
    now = models.SmallIntegerField(choices=(
        (YES, "Keladi"),
        (NO, "Otkaz"),
        (THINKING, "Oylab ko'radi"),
        (NOT_INTERESTING, "Kiyin aloqa")
       
    ),  blank=True, null=True)
    
    coming = models.SmallIntegerField(choices=(
        (ONLINE, "Online"),
        (OFFINE, "Offine")
       
    ),  blank=True, null=True)
    
    
    
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    
    
class Questions(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    text = models.TextField()
    
    
    def __str__(self):
        return self.name  
    
    
    
    
class Modul_Model(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    number_n = models.IntegerField()
    
    def __str__(self):
        return self.name 
        
        
    
    
class Projects(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="images/")   
    url_s = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    
    
    def __str__(self):
        return self.name
       



class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    ONLINE = 0
    OFFINE = 1

    video = models.FileField(upload_to='video', null=True, blank=True)
    url = models.CharField(max_length=150, null=True, blank=True)
    name = models.CharField(max_length=250)



    account_type = models.SmallIntegerField(choices=(
        (ONLINE, "YouTube"),
        (OFFINE, "Video_add")

    ), blank=True, null=True)
    def __str__(self):
        return self.account_type
    
    







class About(models.Model):
    video = models.FileField(upload_to='videos_uploaded/')
    name = models.CharField(max_length=50)
    text = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name







