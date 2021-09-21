from django.db import models

# Create your models here.
# A model is basically a blueprint for your database

class Album(models.Model):
    artist=models.CharField(max_length=250)
    album=models.CharField(max_length=500)
    genre=models.CharField(max_length=100)
    album_logo=models.CharField(max_length=1000)

class Song(models.Model):
    album =models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=250)