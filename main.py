import requests
import streamlit as st
from dotenv import load_dotenv # type: ignore
import os

# MUST be the first Streamlit command
st.set_page_config(page_title="Movie Search App", page_icon="🎬", layout="centered")

# Load environment variables (local safe)
load_dotenv()

# Read API key safely (Cloud + Local)
BASE_URL = "http://www.omdbapi.com/"

try:
    API_KEY = st.secrets["OMDB_API_KEY"]
    BASE_URL = st.secrets.get("BASE_URL", BASE_URL)
except FileNotFoundError:
    API_KEY = os.getenv("OMDB_API_KEY") 
    BASE_URL = os.getenv("BASE_URL", BASE_URL)

# Stop app if API key is missing

if not API_KEY:
    st.error("API key not configured. Please set API_KEY.")
    st.stop()

def get_movie_details(movie:str):
    
    params = {
        "t":movie,
        "apikey":API_KEY
        }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return None, f"Error while connecting to API:, {e}"

    data = response.json()

    if data.get("Response") == "False":
        return None, data.get("Error", "Movie not found")
    
    movie_info = {
        "title": data["Title"],
        "year": data["Year"],
        "genre": data["Genre"],
        "rating": data["imdbRating"],
        "plot": data["Plot"],
        "poster": data.get("Poster")
    }
    return movie_info, None
    
def menu():

    # Basic custom styling for card
    st.markdown("""
    <style>
    .movie-title {
        font-size: 1.6rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }
    .movie-meta {
        font-size: 15px;
        color: #818181;
        margin-bottom: 0.8rem;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🎬 Movie Search App")
    st.subheader("Enter a movie name to fetch details from OMDb API.")

    movie = st.text_input("Movie Name", value="The Matrix")

    if st.button("Search"):
        if not movie.strip():
            st.warning("Movie cannot be empty!")
        else:
            with st.spinner("Searching..."):
                data, error = get_movie_details(movie.strip())

            if error:
                st.error(error)
            elif data:
                st.markdown("<br>", unsafe_allow_html=True)

                col1, col2 = st.columns([1, 2])

                with col1:
                    poster_url = data.get("poster")
                    if poster_url and poster_url != "N/A":
                        st.image(poster_url, use_column_width=True)
                    else:
                        st.write("No poster available")

                with col2:
                    st.markdown(
                        f"<div class='movie-title'>{data['title']} ({data['year']})</div>",
                        unsafe_allow_html=True
                    )
                    st.markdown(
                        f"<div class='movie-meta'>Genre: {data['genre']} • IMDb: {data['rating']}</div>",
                        unsafe_allow_html=True
                    )
                    st.write("**Plot**")
                    st.write(data["plot"])

if __name__ == "__main__":
    menu()
