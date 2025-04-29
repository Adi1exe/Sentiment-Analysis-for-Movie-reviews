import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle  # To save the TF-IDF model for later use

# Load cleaned data
df = pd.read_csv("cleaned_imdb_reviews.csv")

# Initialize TF-IDF Vectorizer
tfidf = TfidfVectorizer(max_features=5000)  # Keep top 5000 words

# Transform text data into numerical vectors
X = tfidf.fit_transform(df["cleaned_review"])  # Convert text to matrix
y = df["sentiment"]  # Labels (0 = negative, 1 = positive)

# Save TF-IDF model for later use
with open("tfidf_vectorizer.pkl", "wb") as f:
    pickle.dump(tfidf, f)

# Save transformed dataset
import scipy.sparse
scipy.sparse.save_npz("tfidf_features.npz", X)  # Save as compressed format
df[["sentiment"]].to_csv("labels.csv", index=False)  # Save labels separately

print("TF-IDF transformation complete. Features saved!")
