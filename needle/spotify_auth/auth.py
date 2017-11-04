import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import os

client_credentials_manager = SpotifyClientCredentials()
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
username = raw_input("Input Username: ")

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



instance = playlist(username)
playlist.get_playlists(instance)

print spotify.user_playlists(username, limit=50, offset=0)



"""    def __init__(self, playlist_name):
        self.playlist_name = playlist_name

    def songs_in_playlist(self, playlist_name):
"""


'''if __name__ == '__main__':
    if token:
        count = 0
        while count < len(spotify.user_playlists(username, limit=50, offset=0)[u'items']):
            print spotify.user_playlists(username, limit=50, offset=0)[u'items'][count][u'name']
            count = count + 1
    else:
        print "Can't get token for", username'''

#if token:
    #playlist class

#else:
    #error
#user_playlist_tracks(user, playlist_id=None, fields=None, limit=100, offset=0, market=None)
