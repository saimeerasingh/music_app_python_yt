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



def delete_all():
    sql = "DELETE  FROM playlist"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM playlist WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(song):
    sql = "UPDATE playlist SET (description, user_id, duration) = (%s, %s, %s, %s) WHERE id = %s"
    values = [song.song_name, song.artist_name, song.video, song.played, song.id]
    run_sql(sql, values)

