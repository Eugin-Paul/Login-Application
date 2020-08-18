from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def register(request) :
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST' :
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for ' + user)
                return redirect('loginpage')
    context = {
    'form' : form
    }
    return render(request,'login/register.html',context)

def loginpage(request) :
    if request.user.is_authenticated:
        return redirect('home')
    else :
        if request.method == 'POST' :
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username = username, password = password)
            if user is not None :
                login(request,user)
                return redirect('home')
            else :
                messages.info(request,'Username OR Password is incorrect')
    context = {
    }
    return render(request,'login/login.html',context)

def logoutpage(request) :
    logout(request)
    context = {
    }
    return redirect('loginpage')

@login_required(login_url = 'loginpage')
def home(request) :
    return render(request,'login/home.html')    
