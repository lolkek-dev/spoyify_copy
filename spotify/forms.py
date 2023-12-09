from django import forms
from . import models
from django.forms.widgets import FileInput

class CustomFileInput(FileInput):
    template_name = "file_input.html"

class MusicForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-line full-width', 'placeholder': 'Название'}))
    preview = forms.FileField(widget=CustomFileInput)

    class Meta:
        model = models.Music
        fields = ('name', 'preview', 'author', 'music_file', 'genre')
