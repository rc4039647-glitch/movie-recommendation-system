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
    if movie:
        result = recommend_movies(movie)

        if isinstance(result, str):
            st.error(result)
        else:
            result.columns = ["Movie", "Match"]
            result["Match"] = (result["Match"] * 100).round(1).astype(str) + "%"

            st.success("Recommended Movies")
            st.dataframe(result, width="stretch")

    else:
        st.warning("Please enter a movie name.")