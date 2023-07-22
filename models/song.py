class Song():
    
    def __init__(self, name, artist_name,genre,played,thumbnail=None):
        self.song_name = name
        self.artist_name = artist_name
        self.song_genre = genre
        self.played = played
        self.thumbnail = thumbnail