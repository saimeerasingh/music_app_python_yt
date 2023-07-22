from flask import Blueprint
# from app import app
from models.playlist import playlist, add_new_song,search_song
from flask import render_template, request, redirect, flash
from models.song import Song

songs_blueprint = Blueprint("playlist",__name__)

@songs_blueprint.route('/playlist')
def index():
    return render_template('index.html',  heading="My Playlist", playlist=playlist)

@songs_blueprint.route('/song', methods=["POST"])
def add_song():
    song_name = request.form["name"]
    song_artist = request.form["artist"]
    song_genre = request.form["genre"]
    new_song = Song(song_name,song_artist,song_genre,False)
    add_new_song(new_song)
    return redirect('/playlist')


@songs_blueprint.route('/results', methods=["POST"])
def search_results():
    found_song = request.form['song_search']
    results = search_song(found_song)
    return render_template('song/show.html' , results=results)