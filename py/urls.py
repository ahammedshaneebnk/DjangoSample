""""py URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# url mapping is here
# r'' means regular expression and inside'' is the actual expression
# first parameter is the user request and next parameter is how to respond to it
# if we write all urls here, then it will be many more and difficult to deal with so
# we create urls.py file in each app and write the urls there and import them to here as one line code for each app
# to do so edit 'from django.conf.urls import url' to 'from django.conf.urls import include, url'
# then include the respective urls.py file inside the []
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # including urls.py file in music directory as follows
    url(r'^music/', include('music.urls')),
]
