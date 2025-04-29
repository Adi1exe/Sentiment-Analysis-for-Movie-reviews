import pandas as pd
import numpy as np
import pickle
import scipy.sparse
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load TF-IDF features and labels
X = scipy.sparse.load_npz("tfidf_features.npz")  # Load numerical features
y = pd.read_csv("labels.csv")["sentiment"]  # Load labels

# Split dataset (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save trained model
with open("sentiment_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Evaluate on test data
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy:.4f}")
print("Classification Report:\n", classification_report(y_test, y_pred))
