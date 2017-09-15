# this file deals the url mapping of this app
# this then will be imported to main page url.py page
# copy the first line import statement of main urls.py page to here
from django.conf.urls import url

# then import views of current directory
# the dot(.) alone represents current directory
from . import views

# providing name space
app_name = 'music'

# copy the syntax structure from main urls.py page and edit it.
# r'' means regular expression
# start with ^ and end with $
urlpatterns = [
    # /music
    url(r'^$', views.index, name='index'),
    # then in views.py file, create a function named as index and tell the response there

    # we need something like this /music/albumId/ for album details eg:- /music/21/
    # for it we need to group the ids together and call it as variable
    # here, (?P<album_id>) is used. ie, in actual, album_id replaces the original id of Album
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]
