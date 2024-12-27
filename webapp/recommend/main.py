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
        "album_id": get_album_id(),
        "recommendations": get_recommendation_results()
    }

def get_urls():
    output = ""
    output += 'open.spotify.com/artist/' + get_artist_id() + '\n'
    output += 'open.spotify.com/track/' + get_song_id() + '\n'
    output += 'open.spotify.com/album/' + get_album_id() + '\n'
    return output

def reset_ids():
    set_album_id('')
    set_artist_id('')
    set_song_id('')

def set_amount(amnt):
    recommend.global_var.amount = amnt

def get_amount():
    return recommend.global_var.amount

def set_type(type):
    recommend.global_var.type = type

def get_type():
    return recommend.global_var.type

def set_check_1(bool):
    recommend.global_var.default = bool

def set_check_2(bool):
    recommend.global_var.mostPopular = bool

def set_check_3(bool):
    recommend.global_var.saveRecent = bool

def set_all_checks(bool):
    set_check_1(bool)
    set_check_2(bool)
    set_check_3(bool)

def get_check_1():
    return recommend.global_var.default

def get_check_2():
    return recommend.global_var.mostPopular

def get_check_3():
    return recommend.global_var.saveRecent

def get_recommendation_results():
    return recommend.global_var.recommendations

def reset_settings():
    set_amount(5)
    set_type('artist')
    set_all_checks(False)

def apply_recommendations():
    seed_id = ''
    if filter == 'artist':
        seed_id = get_artist_id
    elif filter == 'song':
        seed_id = get_song_id
    else:
        seed_id = get_album_id

    if get_check_3() == True:
        recommend.global_var.cached_recommendations = recommend.global_var.recommendations
    if get_check_1() == True:
        recommend.global_var.recommendations = get_recommendations(seed_id, get_amount())
    else:
        recommend.global_var.recommendations = "None"

def get_recommendations(id, limit):
    ##Get Access Token OR use relevant sp call
    ##Call SpotifyAPI with relevant URI
    ##Update recommendation string
    return None

##def get_recommendations with bool parameters for non-default

##Implement mp3 sample and proper result UI