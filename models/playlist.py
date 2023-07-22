from models.song import Song
from ytmusicapi import YTMusic

# song1 = Song("Beautiful","One Direction","Romance",True)
# song2 = Song("Shape","Ed","Fitness",True)
# song3 = Song("Haiye","AR","Fast Beat",False)

playlist = []

def add_new_song(new_song):
    playlist.append(new_song)
    
def search_song(new_song):
    ytmusic = YTMusic(auth="oauth.json")
    results = ytmusic.search(query=new_song,filter="songs",limit=5)
    song_found = set()
    for item in results:
        filtered_song =Song(
            name =item.get("title","Unnamed song"),
            artist_name =item.get("artist","Unknown Artist"),
            video = item.get("videoId","Video Unavailable"))
        song_found.add(filtered_song)
    return song_found