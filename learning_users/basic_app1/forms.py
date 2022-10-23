from socket import fromshare
from django import forms
from django.contrib.auth.models import User
from basic_app1.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    
    
    
    class Meta():
        model=User
        fields=('username','email','password')
        


class UserPortfolioInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')        