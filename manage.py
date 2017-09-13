#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "py.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
    # to run server, just type 'python manage.py runserver'
    # each extra page is called an app in django.
    # to create a new app, just type 'python manage.py startapp appName'
    # almost all needed files such as migration will be automatically added with above command with the new app or page
    # to sync database, just type 'python manage.py migrate'
    # to see sql code of above, type 'python manage.py sqlmigrate music 0001'

    # to open python shell, type 'python manage.py shell' and to exit, 'exit()'
    # to import models to work with, type 'from music.models import Album, Song'
    # to add objects, type 'a = Album(aritst = "Artistname", etc.)'
    # or other way to add object, type 'a.Album()' then 'a.artist="sdf"' like that
    # however to save, 'a.save()'
    # to show respective artist name, 'a.artist' and to show id, 'a.id' or 'a.pk' (primary key)
    # to show all object details, 'Album.objects.all()'
    # to filter showing database, 'Album.objects.filter(artist__startswith='Artist')' for example

    # to create admin credential, 'python manage.py createsuperuser'
    # ahammedshaneebnk hello123
