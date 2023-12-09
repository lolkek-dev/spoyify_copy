# Generated by Django 4.2.2 on 2023-12-09 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spotify', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='avatar',
            field=models.ImageField(upload_to=''),
        ),
        migrations.CreateModel(
            name='FavoriteSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotify.music')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
