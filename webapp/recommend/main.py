import os
import spotipy
import recommend.global_var

from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()
YOUR_APP_CLIENT_ID = os.getenv("YOUR_APP_CLIENT_ID")
YOUR_APP_CLIENT_SECRET = os.getenv("YOUR_APP_CLIENT_SECRET")
YOUR_APP_REDIRECT_URI = os.getenv("YOUR_APP_REDIRECT_URI")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=YOUR_APP_CLIENT_ID,
                                               client_secret=YOUR_APP_CLIENT_SECRET,
                                               redirect_uri=YOUR_APP_REDIRECT_URI,
                                               scope="user-library-read"))

def test_for_artist(name):
    results = sp.search(q='artist:' + name, type='artist', limit=1)
    reset_ids()
    if results['artists']['items'] and name != "":
        set_artist_id(results['artists']['items'][0]['id'])
        return True
    else:
        return False

def test_for_song(name):
    results = sp.search(q='track:' + name, type='track', limit=1)
    reset_ids()
    if results['tracks']['items'] and name != "":
        set_song_id(results['tracks']['items'][0]['id'])
        return True
    else:
        return False

def test_for_album(name):
    results = sp.search(q='album:' + name, type='album', limit=1)
    reset_ids()
    if results['albums']['items'] and name != "":
        set_album_id(results['albums']['items'][0]['id'])
        return True
    else:
        return False

def set_artist_id(id):
    recommend.global_var.artist_id = id

def set_song_id(id):
    recommend.global_var.song_id = id

def set_album_id(id):
    recommend.global_var.album_id = id

def get_artist_id():
    return recommend.global_var.artist_id

def get_song_id():
    return recommend.global_var.song_id

def get_album_id():
    return recommend.global_var.album_id

def upt_page():
    return {
        "title": "Recommendation Results",
        "urls": get_urls(),
        "artist_id": get_artist_id(),
        "song_id": get_song_id(),
        "album_id": get_album_id()
    }

def get_urls():
    output = ""
    output += 'open.spotify.com/artist/' + get_artist_id() + ' '
    output += 'open.spotify.com/track/' + get_song_id() + ' '
    output += 'open.spotify.com/artist/' + get_album_id()
    return output

def reset_ids():
    set_album_id('')
    set_artist_id('')
    set_song_id('')

def set_check_1(bool):
    recommend.global_var.check_1 = bool

def set_check_2(bool):
    recommend.global_var.check_2 = bool

def get_check_1():
    return recommend.global_var.check_1

def get_check_2():
    return recommend.global_var.check_2

def reset_settings():
    set_check_1(False)
    set_check_2(False)

def apply_recommendations():
    if get_check_1() == True:
        return None
    else:
        return None