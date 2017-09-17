# we use generic views
from django.views import generic
from .models import Album
# for creating, updating, deleting views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy  # for helping to delete view
# fro user registration and login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from .forms import UserForm  # form class created in forms.py



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
    # then create template
    # the file name of model form (html) should be 'model name in lower cae + underscore
    # +form' here, model is Album so 'album_form.html' and
    # it should be under music-templates-music directory


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    # on successful delete, redirect to homepage
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    # specify model
    form_class = UserForm
    # once got model, specify template
    template_name = 'music/registration_form.html'

    # separate logic for GET method and POST method

    # new user comes, display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # user fills the form, then process it
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # to get clean data (normalized)
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()  # save to database

            # return User objects if the credentials are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        # return to blank form if form is not valid
        return render(request, self.template_name, {{'form': form}})
        # edit urls.py
