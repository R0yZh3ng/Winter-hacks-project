from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import app


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreatePollForm(ModelForm):
    class Meta:
        model = app
        fields = ['question', 'option_one', 'option_two', 'option_three']