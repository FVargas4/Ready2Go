""" from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint



sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
result = sp.search(search_str)
pprint.pprint(result) """