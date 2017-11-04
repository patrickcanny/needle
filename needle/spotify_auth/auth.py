import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import os

client_credentials_manager = SpotifyClientCredentials()
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#username = raw_input("Input Username: ")
username = 'm31omzzv1u9w52lrj4szxi8qq'

class playlist(object):

    def __init__(self, username):
        self.username = username
        self.playlists = []

    def get_playlists(self):
        count = 0
        while count < len(spotify.user_playlists(self.username, limit=50, offset=0)[u'items']):
            word = spotify.user_playlists(self.username, limit = 50, offset = 0)[u'items'][count][u'name']
            self.playlists.append(word)
            count = count + 1
        print self.playlists
        return(self.playlists)

    def playlists_songs(self):
        count = 0
        for index in self.playlists:
            case = songs(index)
            songs.get_playlist_id(case, count, self.username)
            songs.get_songs(case, self.username)
            count = count + 1

class songs(object):

    def __init__(self, playlist):
        self.playlist = playlist
        self.playlist_id = None
        self.songs = []

    def get_playlist_id(self, count, username):
        tag = spotify.user_playlists(username, limit = 50, offset = 0)[u'items'][count][u'uri']
        self.playlist_id = tag[-22:]

    def get_songs(self, username):
        songs = spotify.user_playlist(username, playlist_id=self.playlist_id, fields=None)
        print songs

class song_info(object):

    def __init__(self,song):
        self.song = song
        


instance = playlist(username)
playlist.get_playlists(instance)
playlist.playlists_songs(instance)
