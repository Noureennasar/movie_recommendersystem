
import streamlit as st
import pickle
import pandas as pd 
import requests


def fetch_poster(movie_id):
  response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=1adcbf8a24f175de15b34c779b5319a1&language=en-US'.format(movie_id))
  data = response.json()
  return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
  movie_index=movies[movies['title'] == movie].index[0]
  distances = similarity[movie_index]
  movies_list = sorted(list(enumerate(distances)),reverse = True, key = lambda x:x[1])[1:8]
  
  recommended_movies=[]
  recommended_movies_posters=[]
  for i in movies_list:
    movie_id = movies.iloc[i[0]].id
    recommended_movies.append(movies.iloc[i[0]].title) #to print title of the movie
    #fetch poster from api
    recommended_movies_posters.append(fetch_poster(movie_id))
  return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Enter your preferred movie name',
    movies['title'].values
)


if st.button('Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

    with col6:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])

    with col7:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])