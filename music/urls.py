# this file deals the url mapping of this app
# this then will be imported to main page url.py page
# copy the first line import statement of main urls.py page to here
from django.conf.urls import url

# then import views of current directory
# the dot(.) alone represents current directory
from . import views

# providing name space
app_name = 'music'

urlpatterns = [
    # /music
    # we are using classes but treat it as view
    url(r'^$', views.IndexView.as_view(), name='index'),

    # eg:- /music/13/
    # for DetailView, it asks for primary key so we use pk instead fo album_id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),
]
