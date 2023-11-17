from django import forms
from . import models


class MusicForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-line full-width', 'placeholder': 'name'}))
    preview = forms.FileInput(attrs={'class': ''})

    class Meta:
        model = models.Music
        fields = ['name', 'preview', 'author', 'music_file', 'genre']
