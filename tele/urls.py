from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('farmerRegister', views.farmerRegister, name='farmerRegister'),
    path('consultantRegister', views.consultantRegister, name='consultantRegister'),
    path('farmerIndex', views.farmerIndex, name='farmerIndex'),
    path('consultantIndex', views.consultantIndex, name='consultantIndex'),
    path('profile', views.profile, name='profile'),
    path('base', views.base, name='base'),

]
