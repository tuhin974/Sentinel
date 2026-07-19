import joblib


class LogDetector:
    def __init__(self):
        self.model = joblib.load("models/anomaly_detector.pkl")
        self.vectorizer = joblib.load("models/vectorizer.pkl")

    def predict(self, log_message):
        features = self.vectorizer.transform([log_message])

        prediction = self.model.predict(features)
        score = self.model.decision_function(features)

        if prediction[0] == -1:
            label = "ANOMALY"
        else:
            label = "NORMAL"

        return label, score[0]