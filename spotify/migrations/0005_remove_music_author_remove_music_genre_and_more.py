# Generated by Django 4.2.2 on 2023-10-24 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0004_remove_music_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='author',
        ),
        migrations.RemoveField(
            model_name='music',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='track',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.DeleteModel(
            name='Genres',
        ),
        migrations.DeleteModel(
            name='Music',
        ),
        migrations.DeleteModel(
            name='PlayList',
        ),
    ]
