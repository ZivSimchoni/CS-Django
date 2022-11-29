from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Take request and return response
# Request is a HttpRequest object
# Response is a HttpResponse object
# Render each request with a template and a context dictionary (optional)

def testPlayground(request):
    return render(request, 'testPlayground.html', {'name': 'Django'})

def login(request):
    return render(request,'login.html')


def register(request):
    return render(request,'register.html')

def forgotpassword(request):
    return render(request,'forgotpassword.html')    