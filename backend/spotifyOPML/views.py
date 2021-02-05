from spotifyOPML.podcasts import Image, OPMLPodcastsPodcast, PodcastPodcast,OPMLPodcasts
from django.shortcuts import render
from django.http import HttpResponse
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import opml
import json


def GetPodcastsFromOPML(request):
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    outline = opml.parse(
        "file:///home/viniciusdof/Downloads/podcasts_opml.xml")

    
    foundPodcastsList = []
    podcastsOPML = OPMLPodcasts(outline.title,foundPodcastsList)
    for val in outline[0]:
        podcastList = []
        podcasts = OPMLPodcastsPodcast(val.text,podcastList)
        result = sp.search(val.text,type="show",market='BR')
        for item in result["shows"]["items"]:
            imageList = []
            for image in item["images"]:
                podcastImage = Image(image["url"],image["height"],image["width"])
                imageList.append(podcastImage)
            podcast = PodcastPodcast(item["name"],item["publisher"],item["id"],item["description"],imageList)
            podcastList.append(podcast)
        podcasts.podcasts = podcastList;
        foundPodcastsList.append(podcasts)
    podcastsOPML.podcasts = foundPodcastsList;
    return HttpResponse(podcastsOPML.toJSON())
