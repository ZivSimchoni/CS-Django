# map urls to views
from django.urls import path
from . import views


# URLconf
# Where to route each request
urlpatterns = [
    path('hello/', views.testPlayground),
    path('login/',views.login),
    path('login/register/',views.register),
    path('login/forgotpassword/',views.forgotpassword)
    ] 
