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
# for easy development, it is good to seperate frontend and backend
# so for it, we use templates. To use it import loader from django.template
from django.template import loader

# define the function named as index
# example


def index(request):
    # we want to display the list of all albums. We access it by python command and assign it into a variable
    all_albums = Album.objects.all()
    # variable for template (we put the template codes under templates/music/ but django automatically look into templates directory )
    template = loader.get_template('music/index.html')
    # creating something as dictionary. more often it is named as context
    # context means information that our template needs
    context = {
        'all_albums': all_albums,
    }
    # view returns response to the request
    # here, we have to return finalized template. Always pass context and request as arguments
    return HttpResponse(template.render(context, request))


# for /music/album_id/ eg:- /music/45/ so we need to pass album_id as parameter
# so we need to connect with database and pull the data
def detail(request, album_id):
    return HttpResponse("<h2>Details of Album ID: " + str(album_id) + "</h2>")

# album_id is integer. We convert it into a string by str() function
