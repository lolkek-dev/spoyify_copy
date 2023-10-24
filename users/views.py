from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from users.forms import *


def sign_up(request):
    form = SignUpForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('users:sign_in')
    return render(request, 'sign_up.html', {'form': form})


def sign_in(request):
    form = SignInForm(data=request.POST)
    if form.is_valid() and request.method == 'POST':
        user = form.get_user()
        login(request, user)
        return redirect('spotify:home')
    return render(request, 'sign_in.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('spotify:home')
