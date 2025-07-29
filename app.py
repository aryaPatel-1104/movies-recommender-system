import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    movies_list = sorted(list(enumerate(similarity2[index])), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for val in movies_list:
        recommended_movies.append(movies.iloc[val[0]].title)

    return recommended_movies

movies_df = pickle.load(open("movies_df.pkl", 'rb'))
movies = pd.DataFrame(movies_df)

similarity2 = pickle.load(open("similarity.pkl", 'rb'))

st.title("Movie Recommeder System")

st.markdown("#### Select or type a Movie name")
selected_movie_name = st.selectbox("", movies['title'].values, index=None)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
