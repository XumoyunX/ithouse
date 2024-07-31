
from django import forms
from main.models import Mentor, Course, New, Users, Open_Class, Video, Projects, Questions, Modul_Model


class Modul_ModelForm(forms.ModelForm):
    class Meta:
        model = Modul_Model()
        fields = '__all__'


class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor()
        fields = '__all__'

class CourseForm(forms.ModelForm):
	class Meta:
		model = Course()
		fields = "__all__"



class NewForm(forms.ModelForm):
	class Meta:
		model = New
		fields = "__all__"
  
  
class UsersForm(forms.ModelForm):
	class Meta:
		model = Users
		fields = "__all__"




class Open_ClassForm(forms.ModelForm):
	class Meta:
		model = Open_Class
		fields = "__all__"
  
  
  
class VideoForm(forms.ModelForm):
	class Meta:
		model = Video
		fields = "__all__" 
  
  
  
class QuestionsForm(forms.ModelForm):
	class Meta:
		model = Questions
		fields = "__all__"    
  
  

class ProjectsForm(forms.ModelForm):
	class Meta:
		model = Projects
		fields = "__all__"    