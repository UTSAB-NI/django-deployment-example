from django.shortcuts import render
from basic_app1.models import User,UserProfileInfo
from basic_app1.forms import UserForm,UserPortfolioInfoForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,'basic_app1/index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    
    registred=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserPortfolioInfoForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
                user=user_form.save()
                user.set_password(user.password)
                user.save()
                
                profile=profile_form.save(commit=False)
                profile.user=user
                
                if 'profile_pic' in request.FILES:
                    profile.profile_pic=request.FILES['profile_pic']
                profile.save()
                
                registred=True
        else:
                print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserPortfolioInfoForm()            
                    
                    
    
    
    
    
    return render(request,'basic_app1/registration.html',{'user_form':user_form,'profile_form':profile_form,'registred':registred})
     
     



def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(usernmae=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            print('someone tried to login and failed')
            print("username:{} and password {}".format(username,password))
            return HttpResponse("invalid login detail supplied") 
    else:
        return render(request,'basic_app1/login.html',{})       
    
    
    
    return render(request,'basic_app1/login.html')     