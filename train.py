import os
import joblib
import pandas as pd

from sklearn.ensemble import IsolationForest
from sklearn.feature_extraction.text import TfidfVectorizer


os.makedirs("models", exist_ok=True)

# Load normal training logs
df = pd.read_csv("data/normal_logs.csv")
logs = df["message"].fillna("").astype(str)

# Convert log messages into numerical features
vectorizer = TfidfVectorizer()
features = vectorizer.fit_transform(logs)

# Train anomaly-detection model
model = IsolationForest(
    n_estimators=100,
    contamination=0.1,
    random_state=42
)

model.fit(features)

# Save model and vectorizer
joblib.dump(model, "models/anomaly_detector.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("Model trained successfully!")
print("Files saved:")
print("- models/anomaly_detector.pkl")
print("- models/vectorizer.pkl")