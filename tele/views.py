from django.shortcuts import render , redirect
from .models import farmerDetails , consultantDetails
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User , auth
# Create your views here.

def index(request):
    return render(request, 'tele/index.html')

def loginpage(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        pasword = request.POST.get('password')
        user = authenticate(request, username=user_name, password=pasword)
        print(user_name,pasword)
        if farmerDetails.objects.filter(user_name=user_name).exists() and farmerDetails.objects.filter(password=pasword).exists():
            curr_user= authenticate(username=user_name,password=pasword)
            if curr_user is not None:
                login(request,curr_user)
                return redirect('/farmerIndex')
        elif consultantDetails.objects.filter(user_name=user_name).exists() and consultantDetails.objects.filter(password=pasword).exists():
            curr_user = authenticate(username=user_name, password=pasword)
            if curr_user is not None:
                login(request, curr_user)
            return redirect('/consultantIndex')
    return render(request, 'tele/login.html')


def consultantRegister(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        qualification = request.POST.get('qualification')
        speciality = request.POST.get('speciality')
        password = request.POST.get('password')
        # repassword = request.POST.get('repassword')
        print(user_name)
        if farmerDetails.objects.filter(user_name=user_name).exists() or consultantDetails.objects.filter(user_name=user_name).exists():
            return redirect('/loginpage')
        currUser = consultantDetails(user_name = user_name , age = age , gender = gender , email = email , phone_number = phone_number , address = address , qualification = qualification ,speciality = speciality , password = password)
        currUser.save()
        user=User.objects.create_user(user_name,email,password)
        user.save()
        return render(request, 'tele/index.html')
    return render(request, 'tele/consultantRegister.html')

def farmerRegister(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        print(user_name,email,phone_number,address,password)
        if farmerDetails.objects.filter(user_name=user_name).exists() or consultantDetails.objects.filter(user_name=user_name).exists():
            return redirect('/loginpage')
        currUser = farmerDetails(user_name = user_name , email = email , phone_number = phone_number , address = address , password = password)
        currUser.save()
        user = User.objects.create_user(user_name, email, password)
        user.save()
        return render(request, 'tele/index.html')
    return render(request, 'tele/farmerRegister.html')

def farmerIndex(request):
    return render(request, 'tele/farmerIndex.html')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/loginpage')

def consultantIndex(request):
    return render(request, 'tele/consultantIndex.html')

def profile(request):
    curr_userobj = farmerDetails.objects.all()
    return render(request, 'tele/profile.html' , {'user':request.user , 'curr_userobj':curr_userobj})

def base(request):
    return render(request, 'tele/base.html')

