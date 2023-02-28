from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'tele/index.html')

def loginpage(request):
    return render(request, 'tele/login.html')

def register1(request):
    return render(request, 'tele/register.html')

