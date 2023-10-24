from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-line full-width', 'placeholder': 'Username'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'input-line full-width', 'placeholder': 'Email'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-line full-width', 'placeholder': 'Password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-line full-width', 'placeholder': ' reenter password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SignInForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'input-line full-width', 'placeholder': 'Username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-line full-width', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']
