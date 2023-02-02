# Genius lyrics on Spotify currently listening
Displays the lyrics of any song currently playing on Spotify on command line in real time.

## General overview
This command line app uses Spotipy (a lightweight Python library for the Spotify Web API) and the Genius API to fetch the name of the song and artist that is currently playing on Spotify and search for the lyrics of said song to display them on the command line, each time a new song starts playing. It also shows some stats of the lyrics and a bit of sentiment analysis.

### Points I would like to improve
- Make a web app for the project so that lyrics can be displayed online and not only on the command line
- Improve the lyric analysis

#### How to use the program
If you want to test this yourself, you'd need to have your own Spotify API Client ID and Client Secret (so that you can access your currently listening songs on your spotify account) and Genius API Client. To get those, go to: <a href="https://developer.spotify.com/" target="_blank">Spotify for Developers</a> and <a href="https://genius.com/api-clients" target="_blank">Genius API</a>

Then, clone the repository and install needed packages. Past your own keys to main.py and run through command line.


<img src="spoti_lyrics.gif"/>
