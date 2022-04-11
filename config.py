

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
USER_ID = "*spotify_user_name*" 
TOKEN = "*spotify_token*"

recently_played_endpoint = "https://api.spotify.com/v1/me/player/recently-played?after={time}"
now_playing_endpoint = "https://api.spotify.com/v1/me/player/currently-playing"
track_endpoint = "https://api.spotify.com/v1/tracks/{id}"
headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {token}".format(token=TOKEN)
    }