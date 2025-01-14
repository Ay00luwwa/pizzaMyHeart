from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2',]
        widgets = {
            'password': forms.PasswordInput(),
        }