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
    results = ytmusic.search(query=new_song,filter="songs",limit=10)
    song_found = set()
    for item in results:
        filtered_song =Song(
            name =item.get("title","Unnamed song"),
            artist_name =get_artist_name(artists=item.get("artists", [{"name":"noname artist"}]) ),
            video = item.get("videoId","Video Unavailable"))
        song_found.add(filtered_song)
    return list(song_found)[:5]

def get_artist_name(artists:list)->str:
  new_set = set()
#   artists = artist_dict.get("artists", [{"name":"noname artist"}]) 
  for a in artists:
    name = a.get("name")
    new_set.add(name)
  return(",".join(new_set))