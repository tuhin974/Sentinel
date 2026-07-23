import joblib
import pandas as pd

# Load the trained model only once
from src.config import load_config

config = load_config()

model = joblib.load(config["model_path"])


def predict_anomaly(features):
    """
    Predict whether the log is normal or an anomaly.
    Returns:
        1  -> Normal
       -1  -> Anomaly
    """

    data = pd.DataFrame([features])

    prediction = model.predict(data)

    return prediction[0]