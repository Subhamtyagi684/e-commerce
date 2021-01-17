from django import forms
from .admin import UserCreationForm
from .models import MyUser
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm, PasswordResetForm

class SignupForm(UserCreationForm):
    class Meta:
        model= MyUser
        fields = ('name','email','mobile')


class PasswordchangeForm(PasswordChangeForm):
    class Meta:
        model = MyUser
        fields = "__all__"


class PasswordresetForm(PasswordResetForm):
    class Meta:
        model = MyUser
        fields = '__all__'

