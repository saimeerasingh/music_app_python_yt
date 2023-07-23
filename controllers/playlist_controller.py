from flask import Blueprint
# from app import app
from models.playlist import playlist, add_new_song,search_song
from flask import render_template, request, redirect, flash
from models.song import Song
import repositories.playlist_repository as playlist_repository

songs_blueprint = Blueprint("playlist",__name__)

@songs_blueprint.route('/playlist')
def index():
    playlist = playlist_repository.select_all()
    return render_template('index.html',  heading="My Playlist", playlist=playlist)

@songs_blueprint.route('/song', methods=["POST"])
def add_song():
    song_name = request.form["name"]
    song_artist = request.form["artist"]
    song_video = request.form["video"]
    new_song = Song(name=song_name,artist_name=song_artist,video=song_video)
    playlist_repository.save(new_song)
    return redirect('/playlist')



@songs_blueprint.route('/results', methods=["POST"])
def search_results():
    found_song = request.form['song_search']
    results = search_song(found_song)
    return render_template('song/show.html' , results=results)


@songs_blueprint.route("/playlist/<id>", methods=['GET'])
def show_song(id):
    song = playlist_repository.select(id)
    return render_template('song/show.html', song=song)

# @songs_blueprint.route("/playlist/<name>/delete", methods=['POST'])
# def delete_song(name):
#     playlist_repository.delete(name=name)
#     return redirect('/playlist')

@songs_blueprint.route("/playlist/<id>/delete", methods=['POST'])
def delete_song(id):
    playlist_repository.delete(id)
    return redirect('/playlist')