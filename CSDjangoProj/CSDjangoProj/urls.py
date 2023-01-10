"""CSDjangoProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Comunication_LTD_Site import views as v
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.loginPage, name="loginPage"),
    path('loginPage/homePage/logout', v.logoutUserPage, name="logoutUserPage"),
    path('registerPage/', v.registerPage, name="registerPage"),
    path('loginPage/homePage/', v.homePage, name="homePage"),
    path('changePassword/', v.change_password, name='change_password'),

    #Reset password
    path('reset_password/', 
    auth_views.PasswordResetView.as_view(template_name="Reset_Password/reset_password.html"),
    name='password_reset'),

    path('reset_password/done', 
    auth_views.PasswordResetDoneView.as_view(template_name="Reset_Password/reset_password_done.html"),
    name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="Reset_Password/reset_password_confirm.html"),
    name='password_reset_confirm'),

    path('reset_password/complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name="Reset_Password/reset_password_complete.html"),
    name='password_reset_complete'),
]
