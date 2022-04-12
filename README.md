# spotify-now-playing-app
a simple spotify now playing app with streamlit

## Run Instructions
- First, you should get your token via spotify account from this link:

    [Spotify token link](https://developer.spotify.com/console/get-recently-played/)

- Then, change the corresponding fields in the 'config.py' file.(user_name and token)

        USER_ID = "*spotify_user_name*" 
        TOKEN = "*spotify_token*"

- Install requirements by :

        pip install -r requirements.txt

- run the app by running this code in terminal:

        streamlit run main.py
