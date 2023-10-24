from django.shortcuts import render
from .models import *
from django.db.models import Q


def home(request):
    music = Music.objects.all()
    return render(request, 'home.html', {'music': music})

def search(request):
    music = Music.objects.all()
    search = request.GET.get('search')
    music = music.filter(
        Q(name__icontains=search)) if search else music
    return render(request, 'search.html', {'music':music})
