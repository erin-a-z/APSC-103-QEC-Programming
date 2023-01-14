import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = '1aecb5ea46cd426e803bcf5243929945'
CLIENT_SECRET = '6da25e9118224e5c8b66ef1f9e76d2a3'

AUTH_URL = 'https://accounts.spotify.com/api/token'

scopes = ["user-follow-read", 'ugc-image-upload', 'user-read-playback-state',
          'user-modify-playback-state', 'user-read-currently-playing', 'user-read-private',
          'user-read-email', 'user-follow-modify', 'user-follow-read', 'user-library-modify',
          'user-library-read', 'streaming', 'app-remote-control', 'user-read-playback-position',
          'user-top-read', 'user-read-recently-played', 'playlist-modify-private', 'playlist-read-collaborative',
          'playlist-read-private', 'playlist-modify-public']

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri='http://127.0.0.1:9090',
                                               scope=scopes))

user_data = sp.currently_playing()
print(user_data)

file1 = open("MyFile.json", "w")
file1.write(str(user_data)) 


