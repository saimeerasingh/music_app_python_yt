from db.run_sql import run_sql
from models.song import Song
from models.playlist import playlist



def save(song):
    sql = "INSERT INTO playlist (song_name, artist_name, video) VALUES (%s, %s, %s) RETURNING *"
    values = [song.song_name, song.artist_name, song.video]
    results = run_sql(sql, values)
    print(song)
    id = results[0]['id']
    song.id = id
    
    return song


def select_all():
    playlist = []
    sql = "SELECT * FROM playlist"
    results = run_sql(sql)
    for row in results:
        song = Song(row['song_name'], row['artist_name'], row['video'], row['id'] )
        playlist.append(song)
    return playlist

def select(id):
    song = None
    sql = "SELECT * FROM playlist WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        song = Song(result['song_name'],result['artist_name'], result['video'], result['id'] )
    return song


def delete_all():
    sql = "DELETE  FROM playlist"
    run_sql(sql)


def delete(name:str):
    sql = f"DELETE FROM playlist WHERE song_name like '{name}'"
    run_sql(sql, name)



