# this file deals the url mapping of this app
# this then willbe imported to main page url.py page
# copy the first line import statement of main urls.py page to here
from django.conf.urls import url
# then import views of current directory
# the dot(.) alone represents current directory
from . import views

# copy the syntax structure from main urls.py page and edit it.
# start with ^ and end with $
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # then in views.py file, create a function named as index and tell the response there
]
