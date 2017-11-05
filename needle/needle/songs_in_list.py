def songs_in_list(self, username):
    songz = []
    tag = spotify.user_playlists(username, limit = 50, offset = 0)[u'items'][0][u'uri']
    playlist_id = tag[-22:]
    _songs = spotify.user_playlist(username, playlist_id)
    if len(songs[u'tracks'][u'items']) > 0:
        count = 0
        while count < len(songs[u'tracks'][u'items']):
            songz.append(songs[u'tracks'][u'items'][count][u'track'][u'name'])
            print songs[u'tracks'][u'items'][count][u'track'][u'name']
            count = count + 1
