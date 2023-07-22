class Song():
    
    def __init__(self, name, artist_name,video,played = False,thumbnail=None):
        self.song_name = name
        self.artist_name = artist_name
        self.played = played
        self.video = video
        self.thumbnail = thumbnail
       