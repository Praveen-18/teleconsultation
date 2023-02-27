from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name='loginpage'),
    path('register1', views.register1, name='register1'),
    path('index', views.index, name='index'),

]
