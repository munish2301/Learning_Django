from django import forms
from secondapp.models import Userinfo,UserProfileInfo
from django.contrib.auth.models import User

class newuser(forms.ModelForm):
    class Meta:
        model=Userinfo
        fields='__all__'
class UserForm(forms.ModelForm):
    password=forms.CharField(widget= forms.PasswordInput() )
    class Meta():
        model=User
        fields=('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio','profile_pic')
