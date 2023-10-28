from django.contrib.auth.models import User
from django.db import models

from spotify.helper import get_audio_length
from spotify.validators import validate_is_audio


class Artist(models.Model):
    avatar = models.ImageField(default='avatar.png')
    nickname = models.CharField(max_length=255)

    def __str__(self):
        return self.nickname




class Genres(models.Model):
    genre_name = models.CharField(max_length=255)
    img  = models.ImageField()

    def __str__(self):
        return self.genre_name



class Music(models.Model):
    name = models.CharField(max_length=255)
    preview = models.ImageField(default='music.png')
    author = models.ForeignKey(Artist, on_delete=models.CASCADE)
    time_length = models.DecimalField(max_digits=20, decimal_places=2, blank=True)
    music_file = models.FileField(validators=[validate_is_audio])
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.time_length:
            audio_length = get_audio_length(self.music_file)
            self.time_length = f'{audio_length:.2f}'

        return super().save(*args, **kwargs)


class PlayList(models.Model):
    name = models.CharField(max_length=255)
    track = models.ManyToManyField(Music)
    artist = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class META:
    ordering = "id"
