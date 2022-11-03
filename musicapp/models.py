
from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Song(models.Model):
    artist = models.ForeignKey(Artiste, related_name = 'songs', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_released = models.DateTimeField('date released')
    likes = models.IntegerField(default=0) 
    

    def __str__(self):
        return self.title


class Lyric(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField()
     

    def __str__(self):
        return self.content     