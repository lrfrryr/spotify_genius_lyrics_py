import os
import spotipy
import lyricsgenius as lg
from waiting import wait
from analyse import analyse_lyrics

os.environ['SPOTIPY_CLIENT_ID'] = "5742d423aa1d48eaa8f6f12ca9aba316"
os.environ["SPOTIPY_CLIENT_SECRET"] ="0607ef519208483297cd5ebafab2960b"
os.environ["SPOTIPY_REDIRECT_URI"] ="http://www.google.com"
os.environ["GENIUS_ACCESS_TOKEN"] = "IinuJ0AR9MTe8daKQZCrIH2et3iIOEm6aGS-tWpcXmnl9n4qqnoM0JoAWlKfyG3x"

spotify_client_id = os.environ['SPOTIPY_CLIENT_ID']
spotify_secret = os.environ["SPOTIPY_CLIENT_SECRET"]
spotify_redirect_uri = os.environ["SPOTIPY_REDIRECT_URI"]
genius_access_token = os.environ["GENIUS_ACCESS_TOKEN"]

scope = "user-read-playback-state"

oauth_object = spotipy.SpotifyOAuth(client_id=spotify_client_id,
                                    client_secret=spotify_secret,
                                    redirect_uri=spotify_redirect_uri,
                                    scope=scope)

token_dict = oauth_object.get_access_token()
token = token_dict["access_token"]

spotify_obj = spotipy.Spotify(auth=token)
genius_obj = lg.Genius(genius_access_token)

currently_playing = spotify_obj.currently_playing()
# print(json.dumps(currently_playing, sort_keys=False, indent=4))


def wait_until():
    progress = spotify_obj.currently_playing()["progress_ms"]
    duration = currently_playing["item"]["duration_ms"]
    if progress == duration:
        return True
    elif progress < 2000:
        return True
    else:

        return False


while True:
    currently_playing = spotify_obj.currently_playing()
    status = currently_playing["currently_playing_type"]

    if status == "track":
        # extract data from the currently playing song
        # to fetch lyrics through genius
        artist_name = currently_playing["item"]["album"]["artists"][0]["name"]
        song_name = currently_playing["item"]["name"]

        song = genius_obj.search_song(title=song_name, artist=artist_name)
        song_lyrics = song.lyrics
        print(song_lyrics)

        # analyse lyrics
        print("")
        print("Here are some lyric stats and somewhat facts:")
        print(analyse_lyrics(song_lyrics))

        wait(lambda: wait_until(), timeout_seconds=4800,
             waiting_for="new song to start")

