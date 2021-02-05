from django.contrib import admin
from django.urls import path
from spotifyOPML import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/opmlpodcastlist', views.GetPodcastsFromOPML),
]
