# views are python functions
# user request something probably a web page or some code and returns something
# or something such as logout, download etc.
# Create your views here.
# deleting 'from django.shortcuts import render' ; don't know why
# there are many methods of giving response, simple one is http response
# writing import statement as 'from django.http import HttpResponse'
from django.http import HttpResponse


# define the function named as index
# example
def index(request):
    return HttpResponse("<h1>This is music app home page</h1>"
                        "<h3>Here you can see a list of all albums</h3>")


# for /music/album_id/ eg:- /music/45/ so we need to pass album_id as parameter
# so we need to connect with database and pull the data
def detail(request, album_id):
    return HttpResponse("<h2>Details of Album ID: " + str(album_id) + "</h2>")
