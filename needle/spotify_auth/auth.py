import sys
import spotipy
import spotipy.util as util
username = raw_input("Input Username: ")
token = util.prompt_for_user_token(username,scope = 'playlist-read-private playlist-read-collaborative playlist-modify-public playlist-modify-private user-read-currently-playing user-library-read',client_id='591ae2a318334c35aabeb516b0c3b0c3',client_secret='6a4c25b2a634486d9ffd30e198ce3a23',redirect_uri='http://localhost/')

spotify = spotipy.Spotify(token)

class playlist(object):

    def __init__(self, username):
        self.username = username
        self.playlists = []

    def get_playlist(self):
        count = 0
        while count < len(spotify.user_playlists(username, limit=50, offset=0)[u'items']):
            playlist = spotify.user_playlists(self.username, limit = 50, offset = 0)[u'items'][count][u'name']
            self.playlists.append(playlist)
            count = count + 1

    def get_songs(self, playlist_name):
        if playlist_name in self.playlists:
            songs = []


        else:
            print "Enter valid playlist name"



"""    def __init__(self, playlist_name):
        self.playlist_name = playlist_name

    def songs_in_playlist(self, playlist_name):
"""


if __name__ == '__main__':
    if token:
        count = 0
        while count < len(spotify.user_playlists(username, limit=50, offset=0)[u'items']):
            print spotify.user_playlists(username, limit=50, offset=0)[u'items'][count][u'name']
            count = count + 1
    else:
        print "Can't get token for", username

#if token:
    #playlist class

#else:
    #error
#user_playlist_tracks(user, playlist_id=None, fields=None, limit=100, offset=0, market=None)
