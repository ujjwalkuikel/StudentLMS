from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request,'login.html')

    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def signupUser(request):
    return render(request,'signup.html')

def about(request):
    return render(request,'about.html')


def handlesignup(request):
    if request.method== "POST":
        username= request.POST('name')
        email= request.POST('email')
        pass1= request.POST('password1')
        pass2= request.POST('password2')
    else:
        HttpResponse('EORROR')


    