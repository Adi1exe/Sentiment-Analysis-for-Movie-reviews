import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download("stopwords")
nltk.download("punkt")

df = pd.read_csv("imdb_reviews.csv")  # Update with your actual dataset path

# Initialize tools
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()

# Text Cleaning Function
def preprocess_text(text):
    text = text.lower()  # Lowercasing
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation & special characters
    tokens = word_tokenize(text)  # Tokenization
    tokens = [word for word in tokens if word not in stop_words]  # Stopword removal
    tokens = [stemmer.stem(word) for word in tokens]  # Stemming
    return " ".join(tokens)

# Apply preprocessing to all reviews
df["cleaned_review"] = df["review"].apply(preprocess_text)

# Save cleaned dataset
df.to_csv("cleaned_imdb_reviews.csv", index=False)

print("Preprocessing complete. Cleaned data saved!")