from SwSpotify import spotify, SpotifyNotRunning

try:
    title, artist = spotify.current()
except SpotifyNotRunning as e:
    print(e)
    exit()

song_info = f"{title} - {artist}"
print(song_info)