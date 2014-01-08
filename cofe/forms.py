from django.conf import settings
from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model

class UserForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput,
        }