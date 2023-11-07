from django import forms
from . import models


class MusicForm(forms.ModelForm):
    class Meta:
        model = models.Music
        fields = ['name', 'preview', 'author', 'music_file', 'genre']
