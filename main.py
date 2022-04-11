import streamlit as st
import functions



if st.button('Get my now playing song on spotify!!'):
    today_listened_df = functions.get_todays_listened_tracks()

    now_playing_df = functions.get_now_playing_track()


    img_url,spotify_url = functions.get_track_by_id(list(now_playing_df.id.unique())[0])

    st.markdown("![Alt Text]({url})".format(url=img_url))
    st.title("{artist}-{song}".format(artist = now_playing_df.artist_name[0] ,song = now_playing_df.song_name[0]))
    st.markdown("## [Play on Spotify!]({})".format(spotify_url))
    st.markdown("### Today Listened Songs")
    st.dataframe(data=today_listened_df[['song_name','artist_name']],width=1000)
        
    
