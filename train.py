import pandas as pd
import joblib

from sklearn.ensemble import IsolationForest
from sklearn.feature_extraction.text import TfidfVectorizer

# Load normal logs
df = pd.read_csv("data/normal_logs.csv")

# Extract log messages
logs = df["message"]

# Convert logs into numerical features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(logs)

# Train anomaly detection model
model = IsolationForest(
    n_estimators=100,
    contamination=0.1,
    random_state=42
)

model.fit(X)

# Save model and vectorizer
joblib.dump(model, "models/anomaly_detector.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("Model trained successfully!")
print("Files saved:")
print(" - models/anomaly_detector.pkl")
print(" - models/vectorizer.pkl")