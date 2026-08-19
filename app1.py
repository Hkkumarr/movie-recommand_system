# ============================================================================
# MOVIE RECOMMENDATION SYSTEM - Streamlit Application
# ============================================================================
# This application uses similarity metrics to recommend movies based on 
# user selection using a Streamlit web interface.
# ============================================================================
import streamlit as st
import pickle
import requests

@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    try:
        response = requests.get(
            f'https://api.themoviedb.org/3/movie/{int(movie_id)}',
            params={
                'api_key': st.secrets['TMDB_API_KEY'],
                'language': 'en-US'
            },
            headers={'User-Agent': 'Mozilla/5.0'},
            timeout=5
        )
        response.raise_for_status()
        poster_path = response.json().get('poster_path')
        return 'https://image.tmdb.org/t/p/w500' + poster_path if poster_path else None
    except (requests.exceptions.RequestException, TypeError, ValueError, KeyError):
        return None

def recommend(movie):
    # Get the index of the selected movie
    movie_index = movies[movies['title'] == movie].index[0]
    
    # Get similarity distances for the selected movie
    distances = similarity[movie_index]
    
    # Sort movies by similarity score and get top 5 (excluding the movie itself)
    movies_list = sorted(
        list(enumerate(distances)), 
        key=lambda x: x[1], 
        reverse=True
    )[1:6]
    
    # Extract recommended movie titles and posters
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id  # Use movie_id, not title
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
            
    return recommended_movies, recommended_movies_posters

# --- DATA LOADING ---
# Load pre-computed similarity matrix and movie data
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pickle.load(open('movies.pkl', 'rb'))

# Extract movie titles for the dropdown menu
movie_list = movies['title'].values

# --- STREAMLIT UI ---
# Set page title
st.title("🎬 Movie Recommendation System")

# Create dropdown for movie selection
select_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movie_list
)

# Recommendation button
if st.button('Get Recommendations'):
    # Get recommended movies
    name,posters = recommend(select_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]
    for i in range(5):
        with columns[i]:
            st.text(name[i])
            if posters[i]:
                st.image(posters[i])
            else:
                st.write('Poster unavailable')

print("Streamlit application is running. Access it at http://localhost:8501")
