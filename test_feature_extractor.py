import pandas as pd
from src.feature_extractor import FeatureExtractor

# Load sample logs
df = pd.read_csv("data/normal_logs.csv")

# Create feature extractor
extractor = FeatureExtractor()

# Convert messages into TF-IDF vectors
features = extractor.fit_transform(df["message"])

print("Feature Matrix Shape:")
print(features.shape)

print("\nSuccess! Feature extraction is working.")