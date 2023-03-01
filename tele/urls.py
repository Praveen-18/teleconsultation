from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('farmerRegister', views.farmerRegister, name='farmerRegister'),
    path('consultantRegister', views.consultantRegister, name='consultantRegister'),
    path('farmerIndex', views.farmerIndex, name='farmerIndex'),
    path('consultantIndex', views.consultantIndex, name='consultantIndex'),
]
