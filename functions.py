import config
import utils
import requests as r
import pandas as pd

def get_todays_listened_tracks():
    today_timestamp = utils.get_today_unix_time()

    response = r.get(config.recently_played_endpoint.format(time=today_timestamp),headers=config.headers)

    data = response.json()

    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

    # Extracting only the relevant bits of data from the json object      
    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])
        
    # Prepare a dictionary in order to turn it into a pandas dataframe below       
    song_dict = {
        "song_name" : song_names,
        "artist_name": artist_names,
        "played_at" : played_at_list,
        "timestamp" : timestamps
    }

    song_df = pd.DataFrame(song_dict, columns = ["song_name", "artist_name", "played_at", "timestamp"])
    return song_df


def get_now_playing_track():

    response = r.get(config.now_playing_endpoint,headers=config.headers)

    data = response.json()
    id_list = []
    song_names = []
    artist_names = []



    # Extracting only the relevant bits of data from the json object      
    id_list.append(data["item"]["id"])
    song_names.append(data["item"]["name"])
    artist_names.append(data["item"]["artists"][0]["name"])


        
    # Prepare a dictionary in order to turn it into a pandas dataframe below       
    song_dict = {
        "id" : id_list,
        "song_name" : song_names,
        "artist_name": artist_names,
  
    }

    song_df = pd.DataFrame(song_dict, columns = ["id","song_name", "artist_name"])
    return song_df


def get_track_by_id(id):
    response = r.get(config.track_endpoint.format(id=id),headers=config.headers)

    data = response.json()

    img_url = data['album']['images'][0]['url']
    spotify_url = data['external_urls']['spotify']
    return img_url,spotify_url



