from flask import Flask
from controllers.playlist_controller import songs_blueprint
from ytmusicapi import YTMusic

ytmusic = YTMusic("oauth.json")

app = Flask(__name__)
app.register_blueprint(songs_blueprint)