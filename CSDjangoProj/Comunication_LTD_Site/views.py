from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('homePage')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('homePage')
            else:
                messages.info(request, 'Username or Password is incorrect')  

        context = {}
        return render(request, "login/loginPage.html", context)  

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('homePage')
    else:
        form = RegisterForm()
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect("loginPage")

        return render(request, "register/register.html", {'form':form})

def logoutUserPage(request):
    logout(request)
    return redirect('loginPage')

@login_required(login_url='loginPage')
def homePage(request):
    return render(request, "home/home.html")

