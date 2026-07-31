import streamlit as st
from system import recommend_movies

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Recommendation System")

st.write("Enter a movie name to get similar movie recommendations.")

movie = st.text_input("Movie Name")

if st.button("Recommend"):
    if movie.strip():
        result = recommend_movies(movie)

        if isinstance(result, str):
            st.error(result)
        else:
            st.dataframe(result, use_container_width=True)
    else:
        st.warning("Please enter a movie name.")