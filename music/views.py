# views are python functions
# user request something probably a web page or some code and returns something
# or something such as logout, download etc.
# Create your views here.
# we want to use information from Album class and Song class so need to import it
from .models import Album, Song
# for easy development, it is good to seperate frontend and backend
# so for it, we use templates.
# combining template loading and running by importing render from shortcuts
# and also avoiding HttpResponse and using render() function
from django.shortcuts import render, get_object_or_404


# 4O4 usually means requested thing is not existing in the resources

# define the function named as index
# example


def index(request):
    # we want to display the list of all albums. We access it by python command and assign it into a variable
    all_albums = Album.objects.all()
    # view returns response to the request
    return render(request, 'music/index.html', {'all_albums': all_albums})
    # actually HttpResponse is binded with render() function inbuilt

# for /music/album_id/ eg:- /music/45/ so we need to pass album_id as parameter
# so we need to connect with database and pull the data
# check the requested album_id existing and displaying respective responses


def detail(request, album_id):
    # try:
    #     album = Album.objects.get(id=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Album doesn't exist")

    # shortcut to replace try and except statements and we need to import get_object_or_4O4
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})
# album_id is integer. We convert it into a string by str() function


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html',
                      {'album': album,
                       'error_message': "You didn't select the valid song!",
                       })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})
