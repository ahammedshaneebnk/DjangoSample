# we use generic views
from django.views import generic
from .models import Album
# for creating, updating, deleting views
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# instead of functions, we now have classes
# it is easy and less no of codes. Here, we have ListView
class IndexView(generic.ListView):
    # specify which template we are using directly here by assigning to template_name
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    # database interaction
    def get_queryset(self):
        return Album.objects.all()


# for details, we use DetailView


class DetailView(generic.DetailView):
    # specify model
    model = Album
    # once got model, specify template
    template_name = 'music/detail.html'


# create album view so inherits from CreateView


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    # then edit url.py
