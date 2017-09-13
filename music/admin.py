from django.contrib import admin
# admin.py is for admin functionality such as creating, deleting users etc.
# Register your models here.

# importing Album class here to play with it
from .models import Album

# make Album appear in the admin page
admin.site.register(Album)
