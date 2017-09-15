from django.contrib import admin
# admin.py is for admin functionality such as creating, deleting users etc.
# Register your models here.

# importing Album class and Song class here to play with it
from .models import Album, Song

# make Album and Song appear in the admin page
admin.site.register(Album)
admin.site.register(Song)
