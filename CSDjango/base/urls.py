from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name="Home"),
    path('login/',views.login, name="Login"),
    path('register/',views.register, name="Register"),
    path('forgotpassword/',views.forgotpassword, name="Forgot Password")
]