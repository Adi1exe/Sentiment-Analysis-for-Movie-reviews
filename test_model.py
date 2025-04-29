import pickle
import scipy.sparse
from sklearn.feature_extraction.text import TfidfVectorizer

# Load saved TF-IDF vectorizer and model
with open("tfidf_vectorizer.pkl", "rb") as f:
    tfidf = pickle.load(f)

with open("sentiment_model.pkl", "rb") as f:
    model = pickle.load(f)

# Function to predict sentiment of a custom review
def predict_sentiment(review):
    review_tfidf = tfidf.transform([review])  # Convert text to TF-IDF
    prediction = model.predict(review_tfidf)[0]
    return "Positive" if prediction == 1 else "Negative"

# Test with user input
while True:
    review = input("\nEnter a movie review (or type 'exit' to stop): ")
    if review.lower() == "exit":
        break
    sentiment = predict_sentiment(review)
    print(f"Sentiment: {sentiment}")
