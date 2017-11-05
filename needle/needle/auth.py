import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import os

client_credentials_manager = SpotifyClientCredentials()
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# username = raw_input("Input Username: ")

class playlist(object):

    def __init__(self, username):
        self.username = username
        self.playlists = []

    def getinfo(self, source):
        data = getattr(self, source)
        return data

    def get_playlists(self):
        count = 0
        while count < len(spotify.user_playlists(self.username, limit=50, offset=0)[u'items']):
            word = spotify.user_playlists(self.username, limit = 50, offset = 0)[u'items'][count][u'name']
            word = str(word)
            self.playlists.append(word)
            count = count + 1

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
        self.rating = 0

    def getinfo(self, source):
        data = getattr(self, source)
        return data

    def get_playlist_id(self, count, username):
        tag = spotify.user_playlists(username, limit = 50, offset = 0)[u'items'][count][u'uri']
        self.playlist_id = tag[-22:]
        return (self.playlist_id)

    def get_songs(self, username):
        songs = spotify.user_playlist(username, playlist_id=self.playlist_id, fields=None)
        if len(songs[u'tracks'][u'items']) > 0:
            count = 0
            while count < len(songs[u'tracks'][u'items']):
                self.songs.append(songs[u'tracks'][u'items'][count][u'track'][u'name'])
                info = song_info(songs[u'tracks'][u'items'][count][u'track'][u'name'])
                song_info.get_info(info, songs, count)
                count = count + 1

    def calculate_rating(self):
            total = 0
            votes = 0
            for index in self.songs:
                total = total + song_info.pos_votes(index)
                votes = votes + song_info.vote_num(index)
            if votes != 0:
                self.rating = (total / votes)
            else:
                self.rating = 0
            return(self.rating)

class song_info(object):

    def __init__(self,song):
        self.song = song
        self.artists = []
        self.album = None
        self.art = None
        self.vote_num = 0
        self.pos_votes = 0

    def getinfo(self, source):
        data = getattr(self, source)
        return data

    def get_info(self, data, value):
        count = 0
        while count < len(data[u'tracks'][u'items'][value][u'track'][u'artists']):
            self.artists.append(data[u'tracks'][u'items'][value][u'track'][u'artists'][count][u'name'])
            count = count + 1

        self.album = data[u'tracks'][u'items'][value][u'track'][u'album'][u'name']
        self.art = data[u'tracks'][u'items'][value][u'track'][u'album'][u'images'][0][u'url']
        return(self.album, self.art, self.artists)



# instance = playlist(username)
# playlist.get_playlists(instance)
# playlist.playlists_songs(instance)
# for playlist in instance.playlists:
#     test = songs(playlist)
#     songs.calculate_rating(test)
