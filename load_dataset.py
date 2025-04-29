import os
import tarfile
import pandas as pd

dataset_path = "aclImdb_v1.tar.gz" 
if not os.path.exists("aclImdb"):
    with tarfile.open(dataset_path, "r:gz") as tar:
        tar.extractall()

def load_imdb_data(directory, label):
    data = []
    path = os.path.join("aclImdb", directory)
    for file in os.listdir(path):
        with open(os.path.join(path, file), "r", encoding="utf-8") as f:
            data.append((f.read(), label))
    return data

train_pos = load_imdb_data("train/pos", 1)
train_neg = load_imdb_data("train/neg", 0)

df = pd.DataFrame(train_pos + train_neg, columns=["review", "sentiment"])

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

print(df.head())

df.to_csv("imdb_reviews.csv", index=False)
print("Dataset saved as imdb_reviews.csv")
