from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-line full-width', 'placeholder': 'Username'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'input-line full-width', 'placeholder': 'Email'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-line full-width', 'placeholder': 'Password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-line full-width', 'placeholder': ' Reenter password'}))

    class Meta:
        error_messages = {"link": {"invalid": "Not really valid"},  # Only change invalid for link-field
                          "required": "You forgot something here!"}  # Change the "required" error for all fields
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SignInForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-line full-width', 'placeholder': 'Username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-line full-width', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class EditProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'gender', 'date_of_birth', 'country', 'city', 'avatar']
