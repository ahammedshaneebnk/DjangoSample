# views are python functions
# user request something probably a web page or some code and returns something
# or something such as logout, download etc.
# Create your views here.
# deleting 'from django.shortcuts import render' ; don't know why
# there are many methods of giving response, simple one is http response
# writing import statement as 'from django.http import HttpResponse'
from django.http import HttpResponse
# we want to use information from Album database so need to import it
from .models import Album

# define the function named as index
# example
def index(request):
    # we want to display the list of all albums. We access it by python command and assign it into a variable
    all_albums = Album.objects.all()
    # defining varaible to put as response
    response_html = ''
    # for each album, the url is different so put in a for loop
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        # making response_html
        response_html += '<a href="' + url + '">' + album.album_title + '</a><br/>'
        # if url is not appearing as a variable then put it inside '' (single quotes) as shown above
        # if 'end of statement expected, message comes, add + before and after the url as shown above
    # view returns response to the request
    return HttpResponse(response_html)


# for /music/album_id/ eg:- /music/45/ so we need to pass album_id as parameter
# so we need to connect with database and pull the data
def detail(request, album_id):
    return HttpResponse("<h2>Details of Album ID: " + str(album_id) + "</h2>")

# album_id is integer. We convert it into a string by str() function
