from django.db import models


# models.py tells about the database. It tells how the data is stored in this particular app
# what tables we need to use in this app (here, music; so album, each album has title, artist and
# another table for songs which has title and other things.)
# so models.py is the blueprint of the database in connection with the particular app
# Create your models here.
# we define each one as class
# each class should inherit from 'models.Model'
# Album class is defined as follows


class Album(models.Model):
    artist = models.CharField(max_length=250)  # CharField means character datatype
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)  # link of image


# the same variable name above will be the column name in database
# there may be many albums
# django automatically differentiate with id
# first album will be assigned as id = 1 and id = 2 for second album etc.
# so primary key is id of album

    # when the details of this Album is called, we want to put some data in return
    # eg:- if in command, 'Album.objects.all()' is called we want to return
    # some information about this, here we give album title and artist as follows
    def __str__(self):  # built in string representation of object
        return self.album_title + ' - ' + self.artist

# Song class is defined as follows
# but we want to link Song with Album
# An album may contain many songs but A song will be associated with an album
# so there is a connection with Song class and Album class
# we have to put that connection in below
# we use ForeignKey for that purpose


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)  # Song is linked to Album
    # 'on_delete=models.CASCADE' means when an album is deleted, all songs associated-
    # with that album should also be deleted
    # in some cases it may not be needed
    file_type = models.CharField(max_length=10)  # mp3 or avi or like that
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):  # built in string representation of object
        return self.song_title

# when this is finished, then main settings.py must be changed
# under the INSTALLED APP section we want add something about the music app
# it is as follows 'music.apps.MusicConfig' ie, in music directory, apps.py file-
# there will be a function called MusicConfig. it is included in the main settings.py file

# even though we have defined the blueprint of database, it is not synced with the original database
# to do it just type as command line 'python manage.py makemigrations music'
# then run migration my 'python manage.py migrate'
# now the database is synced with the above code
