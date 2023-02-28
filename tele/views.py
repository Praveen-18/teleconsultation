from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'tele/index.html')

def loginpage(request):
    return render(request, 'tele/login.html')

def consultantRegister(request):
    return render(request, 'tele/consultantRegister.html')

def farmerRegister(request):
    return render(request, 'tele/farmerRegister.html')


