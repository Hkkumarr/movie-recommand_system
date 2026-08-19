# movie-recommand_system
🎬 Movie Recommendation System

A Movie Recommendation System built with Python and Streamlit that recommends movies based on the movie selected by the user. The system uses a pre-computed similarity matrix to identify movies that are most similar to the selected movie and displays their posters using the TMDB API.

📌 Features
🎬 Select a movie from a dropdown menu.
🤖 Generate the top 5 similar movie recommendations.
📊 Uses a pre-computed similarity matrix for recommendations.
🖼️ Fetches movie posters dynamically from TMDB.
🔐 Keeps the TMDB API key secure using Streamlit Secrets.
🌐 Simple and interactive Streamlit web interface.
🔄 Includes retry handling for TMDB API requests.
⚠️ Displays "Poster unavailable" when a poster cannot be fetched.
🛠️ Technologies Used
Python
Streamlit – Web application interface
Pandas – Movie dataset handling
Pickle – Loading pre-trained movie data and similarity matrix
Requests – TMDB API requests
Scikit-learn – Used during the model/data-preparation stage
TMDB API – Movie poster and movie information
📂 Project Structure
movie_recommendation_project/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── .gitignore
│
└── .streamlit/
    └── secrets.toml
File Description
File	Description
app.py	Main Streamlit application
movies.pkl	Preprocessed movie dataset
similarity.pkl	Pre-computed movie similarity matrix
requirements.txt	Required Python libraries
.gitignore	Prevents sensitive/unnecessary files from being uploaded
secrets.toml	Stores the TMDB API key securely
⚙️ How the System Works

The recommendation process follows these steps:

User selects a movie
        ↓
Find selected movie index
        ↓
Get similarity scores
        ↓
Sort movies by similarity
        ↓
Select top 5 similar movies
        ↓
Get movie IDs
        ↓
Request posters from TMDB API
        ↓
Display recommendations
Recommendation Logic

The application finds the selected movie in the movies DataFrame:

movie_index = movies[movies['title'] == movie].index[0]

It then retrieves the similarity scores:

distances = similarity[movie_index]

The movies are sorted according to their similarity scores, and the top 5 recommendations are selected.

🔑 TMDB API Configuration

The application uses a TMDB API key through Streamlit Secrets.

Create:

.streamlit/secrets.toml

Add:

TMDB_API_KEY = "YOUR_TMDB_API_KEY"

Important: Never put your real API key directly inside app.py, and never commit secrets.toml to GitHub.

Add this to .gitignore:

.streamlit/secrets.toml

For Streamlit Cloud, add the same secret through the application's Secrets settings.

📦 Installation
1. Clone the Repository
git clone YOUR_GITHUB_REPOSITORY_URL
cd movie_recommendation_project
2. Create a Virtual Environment

Using Python:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt

Example requirements.txt:

streamlit
pandas
requests
scikit-learn
▶️ Run the Application

Start the Streamlit application using:

streamlit run app.py

The application will normally be available at:

http://localhost:8501
🖥️ Application Interface

The application provides:

Movie selection dropdown
Get Recommendations button
Five recommended movies
Movie posters
Fallback message when a poster is unavailable

Example:

🎬 Movie Recommendation System

Select a movie to get recommendations:
[ Avatar                         ▼ ]

        [ Get Recommendations ]

Movie 1       Movie 2       Movie 3       Movie 4       Movie 5
Poster        Poster        Poster        Poster        Poster
📊 Dataset Requirements

The movies.pkl file should contain at least these columns:

movie_id
title

Example:

movie_id	title
19995	Avatar
285	Pirates of the Caribbean
206647	Spectre

The movie_id is used to request the corresponding poster from TMDB.

🧠 Similarity Matrix

The similarity.pkl file contains pre-computed similarity values between movies.

For example:

             Avatar   Spectre   Titanic
Avatar        1.00      0.32      0.75
Spectre       0.32      1.00      0.28
Titanic       0.75      0.28      1.00

When a user selects Avatar, the system finds movies with the highest similarity scores and returns the top 5, excluding Avatar itself.

🔐 Security

Do not write your API key directly in Python:

# ❌ Do not do this
api_key = "your-real-api-key"

Instead, use:

# ✅ Recommended
api_key = st.secrets["TMDB_API_KEY"]

Also make sure the secret file is included in .gitignore.

🚀 Deployment

The project can be deployed using Streamlit Community Cloud.

General deployment process:

GitHub Repository
       ↓
Push project files
       ↓
Connect repository to Streamlit Cloud
       ↓
Select app.py
       ↓
Add TMDB_API_KEY in Secrets
       ↓
Deploy
       ↓
Get public application URL

Before deployment, make sure that:

app.py is present.
movies.pkl is uploaded.
similarity.pkl is uploaded.
requirements.txt is present.
API key is stored in Streamlit Secrets.
API key is not committed to GitHub.
⚠️ Common Issues
1. KeyError: 'TMDB_API_KEY'

Make sure your Streamlit secret contains:

TMDB_API_KEY = "YOUR_TMDB_API_KEY"
2. Movie Poster Not Showing

Possible reasons:

Invalid TMDB movie ID.
Movie does not have a poster.
TMDB API request failed.
API key is invalid.
Internet/API connection problem.

The application handles these cases by displaying:

Poster unavailable
3. FileNotFoundError

If you see:

FileNotFoundError: similarity.pkl

make sure similarity.pkl is in the same directory as app.py.

4. Large similarity.pkl

The similarity matrix can be very large. If the file is too large for normal GitHub uploads, consider using Git LFS or another suitable model/data-storage solution.

🔮 Future Improvements
🔍 Add movie search functionality.
⭐ Display movie ratings.
📅 Display release year.
🎭 Add genre filters.
📝 Show movie descriptions.
❤️ Add user-based recommendations.
👤 Add user login and personalized recommendations.
⚡ Optimize the similarity matrix for faster deployment.
📱 Improve mobile responsiveness.
☁️ Deploy the complete application online.
📜 Disclaimer

This project is created for educational and demonstration purposes. Movie information and posters are retrieved through the TMDB API. The project is not affiliated with or endorsed by TMDB.

👨‍💻 Author

Harshit Sharma

Project

Movie Recommendation System using Python, Machine Learning & Streamlit

⭐ If you find this project useful, consider giving the repository a star on GitHub.