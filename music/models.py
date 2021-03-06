from django.db import models
from django.core.urlresolvers import reverse


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()  # to enable file browsing

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):  # built in string representation of object
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)  # Song is linked to Album
    file_type = models.CharField(max_length=10)  # mp3 or avi or like that
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):  # built in string representation of object
        return self.song_title
