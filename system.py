import pandas as pd
import numpy as np
import sklearn 

print(pd.__version__)
print(np.__version__)
print(sklearn.__version__)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.DataFrame({
    "title": [
        "Interstellar", "Inception", "The Martian", "Arrival",
        "The Matrix", "Avatar", "Titanic", "The Notebook",
        "Avengers: Endgame", "Iron Man", "Jurassic Park", "The Dark Knight"
    ],
    "description": [
        "space science fiction astronauts future adventure",
        "science fiction dreams technology thriller mind bending",
        "space science fiction astronaut survival mars adventure",
        "science fiction aliens language space mystery",
        "science fiction technology artificial intelligence action",
        "science fiction space aliens adventure fantasy",
        "romance drama ship ocean historical tragedy",
        "romance relationship love drama emotional",
        "superhero action marvel time travel adventure",
        "superhero action technology marvel engineering",
        "dinosaurs science adventure action island",
        "superhero action crime batman thriller"
    ]
})

movies

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

movie_vectorizer = TfidfVectorizer(stop_words="english")

movie_matrix = movie_vectorizer.fit_transform(
    movies["description"]
)

print("Movie matrix shape:", movie_matrix.shape)

from sklearn.metrics.pairwise import cosine_similarity

similarity_matrix = cosine_similarity(movie_matrix)

print("Similarity matrix shape:", similarity_matrix.shape)

def recommend_movies(movie_title, number_of_recommendations=5):
    if movie_title not in movies["title"].values:
        return f"Movie '{movie_title}' was not found."

    movie_index = movies.index[
        movies["title"] == movie_title
    ][0]

    similarity_scores = list(
        enumerate(similarity_matrix[movie_index])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    similarity_scores = [
        item for item in similarity_scores
        if item[0] != movie_index
    ]

    recommendations = []

    for index, score in similarity_scores[:number_of_recommendations]:
        recommendations.append({
            "movie": movies.iloc[index]["title"],
            "similarity": round(score, 3)
        })

    return pd.DataFrame(recommendations).reset_index(drop=True)

recommend_movies("Interstellar")    
recommend_movies("Iron Man")
recommend_movies("Titanic")
