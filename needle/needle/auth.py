import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import os


def getUser(_username):
    client_credentials_manager = SpotifyClientCredentials()
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    username = _username
    return spotify

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

    """def get_songs(self, playlist_name):
        if playlist_name in self.playlists:
            songs = []
            user_playlist_tracks(user, playlist_id=None, fields=None, limit=100, offset=0, market=None)

        else:
            print "Enter valid playlist name" """

class songs(object):

    def __init__(self, playlist):
        self.playlist = playlist
        self.songs = []

    #def get_songs(self):
