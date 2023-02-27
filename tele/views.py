from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'tele/index.html')

def loginpage(request):
    return render(request, 'tele/loginpage.html')

def register1(request):
    return render(request, 'tele/register1.html')

