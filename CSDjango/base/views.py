from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'Home.html')

def login(request):
    return render(request,'login.html')


def register(request):
    return render(request,'register.html')

def forgotpassword(request):
    return render(request,'forgotpassword.html') 
