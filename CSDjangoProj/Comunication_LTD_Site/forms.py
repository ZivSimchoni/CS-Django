from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        fields = ["old_password ", "new_password1", "new_password2"]

