import joblib
import pandas as pd

from src.config import load_config

config = load_config()

model = joblib.load(config["model_path"])


def predict_anomaly(features):
    """
    Predict whether the log is normal or anomalous.

    Returns
    -------
    tuple
        (prediction, score)
    """

    data = pd.DataFrame([features])

    prediction = model.predict(data)[0]

    score = model.decision_function(data)[0]

    return prediction, score