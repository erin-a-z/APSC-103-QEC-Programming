import spotipy, requests
from spotipy.oauth2 import SpotifyOAuth
from urllib.request import urlopen
import re
import geocoder
import time
from flask import Flask, render_template


# function to get current IP
def getIP():
	d = str(urlopen('http://checkip.dyndns.com/').read())
	return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)

CLIENT_ID = '9b4d7253dc844637bd8d7820782d3845'
CLIENT_SECRET = 'f6e73043407f49c09e67fa6cdd04fbd0'

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

cache = open('.cache', 'r')
cacheContent = cache.read()
access_token = re.findall(r"\".*?\"",cacheContent)
access_token = access_token[1].replace('"','')

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'


# get current user ID

r = requests.get(BASE_URL + 'me/', headers=headers)

r_data = r.json()
link = r_data['href']

regexFindUserId = re.findall(r"users/.*?$",link)
userID = regexFindUserId[0][6:]

print(userID)
def createPlaylist():
    # create playlist
    r = requests.get(BASE_URL + 'users/{user_id}/playlists'.format(user_id=userID), headers=headers)
    playlistID = ''
    return playlistID
    # psudo code for creating playlist
    # reference:https://developer.spotify.com/console/post-playlists/

    # request body 
    # {
    #   "name": "location {number}",
    #   "description": "playlist for location {number}",
    #   "public": false
    # }


def playPastSongs():
    playlist_id = 'your_playlist_id'
    sp.start_playback(context_uri=f'spotify:playlist:{playlist_id}')
    # plays the songs the user have played before at that certain location

playbackStatus = sp.current_playback()
# Location check
previousIP = 's'
IPs = []
locations = []

playlist_id = createPlaylist()
# if the user is playing music i.e. not paused
if str(playbackStatus) != 'None':
    # save the location
    currentIP = getIP()
    print("IP: " + currentIP)
    # Detect whether the ip has changed

    if previousIP == currentIP:
        pass
        # the user has not moved
        # add the song currently playing to the current playlist
        # reference https://developer.spotify.com/console/post-playlist-tracks/
        r = requests.get(BASE_URL + 'playlists/{playlist_id}/tracks'.format(playlist_id=playlist_id), headers=headers)
    else:
        playlist_id = createPlaylist()
    IPs.append(currentIP)
    g = geocoder.ip('me')
    print(g.latlng)
    locations.append(g)
else:
    print("not playing anything")
    

# append songs to the playlist created 
outputFile = open("output.json", "w")
outputFile.write(str(playbackStatus))

# launch a webpage with a button indicating whether the user want to play the playlist for the current location

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play_past_songs')

if __name__ == '__main__':
    app.run(debug=True)


