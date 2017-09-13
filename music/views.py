# views are python functions
# user request something probably a webpage and something returns
# or something such as logout, download etc.
# Create your views here.
# deleting 'from django.shortcuts import render' ; don't know why
# there are many methods of giving response, simple one is http response
# writing import statement as 'from django.http import HttpResponse'
from django.http import HttpResponse


# define the function named as index
# example
def index(request):
    return HttpResponse("<h1>This is music app home page</h1>")
