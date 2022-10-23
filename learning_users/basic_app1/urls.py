from django.contrib import admin
from django.urls import path,include
from basic_app1 import views
import basic_app1


app_name='basic_app1'


urlpatterns = [
    
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login')
]
