from dataclasses import dataclass
from typing import List
import json

@dataclass
class Image:
    url: str
    height: int
    width: int
    def __init__(self,url,height,width):
        self.url = url
        self.height = height
        self.width = width

@dataclass
class PodcastPodcast:
    name: str
    publisher: str
    id: str
    description: str
    images: List[Image]
    def __init__(self,name,publisher,id,description,images):
        self.name = name
        self.publisher = publisher
        self.id = id
        self.description = description
        self.images = images



@dataclass
class OPMLPodcastsPodcast:
    searchedName: str
    podcasts: List[PodcastPodcast]
    def __init__(self,searchedName,podcasts):
        self.searchedName = searchedName
        self.podcasts = podcasts


@dataclass
class OPMLPodcasts:
    title: str
    podcasts: List[OPMLPodcastsPodcast]
    def __init__(self,title,podcasts):
        self.title = title
        self.podcasts = podcasts
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
