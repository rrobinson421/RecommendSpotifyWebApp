import os
import spotipy
import recommend.global_var
import base64
import requests
import json

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

def get_token_basic():
    auth_header = base64.b64encode(f"{YOUR_APP_CLIENT_ID}:{YOUR_APP_CLIENT_SECRET}".encode()).decode()
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_header}"
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json().get("access_token")

##TODO: Set up Guest Account Authentication
##TODO: Remove testing methods
##TODO: Update Nav Bar for Login support

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
        "recommendations": get_recommendation_results
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
    filter = recommend.global_var.type
    seed_artists = [get_artist_id()]
    seed_tracks = [get_song_id()]
    seed_genres = []

    if get_check_3() == True:
        recommend.global_var.cached_recommendations = recommend.global_var.recommendations
    if get_check_1() == True:
        ##recommend.global_var.recommendations = get_recommendations_default(seed_artists, seed_tracks, seed_genres, get_amount(), filter)
        recommend.global_var.recommendations = get_recommendations_test()
        print(recommend.global_var.recommendations)
    else:
        recommend.global_var.recommendations = "None"

def get_recommendations_default(seed_artists, seed_tracks, seed_genres, lim, filter):
    if not recommend.global_var.logged_in:
        token = get_token_basic()
    else:
        token = get_token_basic()
    url = "https://api.spotify.com/v1/recommendations"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "seed_artists": ",".join(seed_artists) if seed_artists and seed_artists != '' else None,
        "seed_tracks": ",".join(seed_tracks) if seed_tracks and seed_tracks != '' else None,
        "seed_genres": ",".join(seed_genres) if seed_genres else None,
        "limit": lim
    }
    recommendation_json = requests.get(url, headers=headers, params=params)
    recommendation_json.raise_for_status()
    return parse_json(recommendation_json, filter)

def get_recommendations_test():
    filter = 'song'
    token = get_token_basic()
    url = "https://api.spotify.com/v1/recommendations?seed_artists=&seed_tracks=4TGZTPJ50VXfqCIEwf6Bmm&limit=5"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    rec_test = requests.get(url, headers=headers)
    rec_test.raise_for_status()
    return parse_json(rec_test, filter)
    
def parse_json(json, filter):
    return "got json"