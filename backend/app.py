from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv
import joblib
import re

load_dotenv()
OMDB_API_KEY = os.getenv("OMDB_API_KEY")

app = Flask(__name__)

current_dir = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(current_dir, "sentiment_model.pkl"))
vectorizer = joblib.load(os.path.join(current_dir, "tfidf_vectorizer.pkl"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/movie", methods=["GET"])
def get_movie():
    movie_name = request.args.get("title")
    if not movie_name:
        return jsonify({"error": "Please provide a movie title"}), 400

    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "False":
        return jsonify({"error": "Movie not found"}), 404

    return jsonify({
        "title": data.get("Title"),
        "year": data.get("Year"),
        "imdb_rating": data.get("imdbRating"),
        "poster": data.get("Poster"),
        "plot": data.get("Plot"),
    })

@app.route("/analyze", methods=["POST"])
def analyze_sentiment():
    data = request.get_json()
    review_text = data.get("review", "")

    if not review_text:
        return jsonify({"error": "No review provided"}), 400

    cleaned_text = re.sub(r"[^a-zA-Z\s]", "", review_text).lower()
    vectorized_text = vectorizer.transform([cleaned_text])

    sentiment = model.predict(vectorized_text)[0]
    sentiment_label = "Positive 😊" if sentiment == 1 else "Negative 😞"

    return jsonify({"sentiment": sentiment_label})

@app.route("/suggest", methods=["GET"])
def suggest_movies():
    query = request.args.get("query", "").strip()
    if not query:
        return jsonify({"error": "No query provided"}), 400

    omdb_url = f"https://www.omdbapi.com/?s={query}&apikey={OMDB_API_KEY}"
    response = requests.get(omdb_url)
    data = response.json()

    if "Search" in data:
        return jsonify(data["Search"])
    else:
        return jsonify({"error": "No results found"}), 404

if __name__ == "__main__":
    app.run(debug=True)