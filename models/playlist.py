from models.song import Song
from ytmusicapi import YTMusic

song1 = Song("Beautiful","One Direction","Romance",True)
song2 = Song("Shape","Ed","Fitness",True)
song3 = Song("Haiye","AR","Fast Beat",False)

playlist = [song1,song2,song3]

def add_new_song(new_song):
    playlist.append(new_song)
    
def search_song(new_song):
    ytmusic = YTMusic(auth="oauth.json")
    results = ytmusic.search(query=new_song)
    titles = set()
    for item in results:
      if "title" in item:
        titles.add(item["title"])
    return titles