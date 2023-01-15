from django.shortcuts import render, redirect
from .forms import RegisterForm, ChangePasswordForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from . badAuth import SettingsBackend
from django.contrib.auth.models import User


# Create your views here.

#################################   SECURED APP   ###################################

#from django.contrib.auth import authenticate
# def loginPage(request):
#     if request.user.is_authenticated:
#         return redirect('homePage')
#     else:
#         if request.method == "POST":
#             username = request.POST['username']
#             password = request.POST['password']

#             user = authenticate(request, username=username, password=password)
#             print(user)
#             if user is not None:
#                 login(request, user)
#                 return redirect('homePage')
#             else:
#                 messages.info(request, 'Username or Password is incorrect')  

#         context = {}
#         return render(request, "login/loginPage.html", context) 


# def registerPage(request):
#     if request.user.is_authenticated:
#         return redirect('homePage')
#     else:
#         form = RegisterForm()
#         if request.method == "POST":
#             form = RegisterForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 user = form.cleaned_data.get('username')
#                 messages.success(request, 'Account was created for ' + user)

#                 return redirect("loginPage")

#         return render(request, "register/register.html", {'form':form})

def logoutUserPage(request):
    logout(request)
    return redirect('loginPage')

@login_required(login_url='loginPage')
def homePage(request):
    return render(request, "home/home.html")

@login_required(login_url='loginPage')
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request,'Your password was successfully updated!\nPlease login with the new password')
            return redirect('logoutUserPage')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'Change_password/change_password.html', {'form': form})


#################################   UNSECURED APP   ###################################

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('homePage')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = SettingsBackend.authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('homePage')
            else:
                messages.info(request, 'Username or Password is incorrect')  

        context = {}
        return render(request, "login/loginPage.html", context) 

from django.db import connection

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('homePage')
    else:
        form = RegisterForm()
        if request.method == "POST":
            form = RegisterForm(request.POST)
            try:
                user = form.save(commit=False)
                if(user.username[0] == "'" or user.username[0] == '"' or user.username == 'username'):
                    cursor=connection.cursor()
                    cursor.execute(f"SELECT username FROM auth_user WHERE username LIKE {user.username}")
                    r=cursor.fetchall()
                    messages.error(request, r)
            except:
                pass           
                 
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect("loginPage")

        return render(request, "register/register.html", {'form':form})

