import numpy as np
import pandas as pd
import streamlit as st
import requests

st.set_page_config(layout='wide')
st.markdown('## Anime Recommender System')
st.markdown("'Made For Weebs' by Umang Kirit Lodaya - A Weeb Extraordinaire! | [GitHub](https://github.com/Umang-Lodaya/Anime-Recommender-System) | [LinkedIn](https://www.linkedin.com/in/umang-lodaya-074496242/) | [Kaggle](https://www.kaggle.com/umanglodaya)")
st.markdown("")

def get_anime_poster(anime_name):
    # Format the anime name for the API request
    formatted_name = anime_name.replace(' ', '%20')

    # Make a request to Jikan API v4 to search for the anime
    url = f"https://api.jikan.moe/v4/anime?q={formatted_name}"
    response = requests.get(url)
    data = response.json()

    # Retrieve the poster image URL from the API response
    if 'data' in data and data['data']:
        anime = data['data'][0]
        poster_url = anime['images']['jpg']['image_url']
        return poster_url

    return 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrEWuSqni9XNT5-8iTTJIZgFkBOhhyaQesaQzScsTZUc0uJd4nfIbvmJWN7m8txq5ojZ4&usqp=CAU'


df = pd.read_csv('Anime.csv')
titles = list(df['Name'])
r = pd.read_csv('similarity.csv')
w = 150

def recommend(anime):
    ID = df[df['Name'] == anime].index[0]
    vector = r.iloc[ID, :].values[1:6]
    recommended = []
    for i in vector:
        recommended.append(df.iloc[i].Name)
    
    return recommended

selected = st.selectbox('Search an anime', titles)
if st.button('Recommend Animes'):
    a, b, c, d, e = recommend(selected)

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.image(get_anime_poster(a), width=w)
    col1.write(a)
    
    col2.image(get_anime_poster(b), width=w)
    col2.write(b)
    
    col3.image(get_anime_poster(c), width=w)
    col3.write(c)
    
    col4.image(get_anime_poster(d), width=w)
    col4.write(d)
    
    col5.image(get_anime_poster(e), width=w)
    col5.write(e)