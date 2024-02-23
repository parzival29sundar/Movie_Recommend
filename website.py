import streamlit as st
import pickle
import pandas as pd
import requests #to hit api

def fetch_poster(id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=29f19566be60cbd15ccf061e50faf274&language=en-US'.format(id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" +data['poster_path']

def recommend(movie):
    movie_index = movies[movies['original_title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse =True , key = lambda x: x[1])[1:6]

    recommended_movies=[]
    recommend_movies_posters=[]


    for i in movies_list:
        id = movies.iloc[i[0]].id
        #to fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].original_title)
        #fetching poster
        recommend_movies_posters.append(fetch_poster(id))
    return recommended_movies,recommend_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies= pd.DataFrame(movies_dict)

similarity =  pickle.load(open('similarity.pkl', 'rb'))




st.title(':blue[Movie Recommender System]')

selected_movie_name = st.selectbox(
    'Enter a movie name',
    movies['original_title'].values
)


if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

    col1 , col2 , col3 , col4 , col5 , = st.columns(5)
    with col1:
        # st.text(names[0])
        st.image(posters[0], caption=names[0], use_column_width=True, output_format="JPEG", clamp=True, width=50)
    with col2:
        # st.text(names[1])
        st.image(posters[1], caption=names[1], use_column_width=True, output_format="JPEG", clamp=True)
    with col3:
        # st.text(names[2])
        st.image(posters[2], caption=names[2], use_column_width=True, output_format="JPEG", clamp=True)
    with col4:
        # st.text(names[3])
        st.image(posters[3], caption=names[3], use_column_width=True, output_format="JPEG", clamp=True)
    with col5:
        # st.text(names[4])
        st.image(posters[4], caption=names[4], use_column_width=True, output_format="JPEG", clamp=True)


