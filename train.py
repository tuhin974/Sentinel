import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Loading the training data
data = pd.read_csv("data/normal_logs.csv")

print(f"Loaded {len(data)} training samples.")

# Isolation forest model training
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

#training
model.fit(data)

#save
joblib.dump(model, "models/model.pkl")

print("\n✅ Model trained successfully!")
print("✅ Model saved as models/model.pkl")