from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
import random
from . import forms


def home(request):
    music = Music.objects.all()
    return render(request, 'home.html', {'music': music})


def search(request):
    music = Music.objects.all()
    search = request.GET.get('search')
    genre = Genres.objects.all()
    music = music.filter(
        Q(name__icontains=search)) if search else music
    return render(request, 'search.html', {'music': music, 'genre': genre})


def music(request, pk):
    music = Music.objects.get(pk=pk)
    return render(request, 'music.html', {'music': music})


def afternext(request):
    all_music = Music.objects.all()
    random_number = random.randint(1, len(all_music))
    action = request.GET.get('action')
    random_number = random.randint(1, len(all_music))
    if action == "after":
        music = Music.objects.get(pk=random_number)
        return render(request, 'music.html', {'music': music})
    if action == "next":
        music = Music.objects.get(pk=random_number)
        return render(request, 'music.html', {'music': music})


def randommusic(request):
    all_music = Music.objects.all()
    random_number = random.randint(1, len(all_music))
    random_music = Music.objects.get(pk=random_number)
    return render(request, 'random.html', {'random_music': random_music})

def MusicAdd(request):
    form = forms.MusicForm(request.POST or None, request.FILES)
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('spotify:home')
    form = forms.MusicForm()
    return render(request, 'music_add.html', {'form': form})