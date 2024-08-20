from django import forms
from .models import Users

# class UsersFrom(forms.ModelForm):
#     class Meta:
#         model = Users
#         fields = ['course', 'name', 'number']
#
#


class YourForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['course', 'name', 'number']