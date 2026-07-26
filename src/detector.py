import re
import joblib


class LogDetector:

    def __init__(
        self,
        model_path="models/anomaly_detector.pkl",
        vectorizer_path="models/vectorizer.pkl"
    ):
        from pathlib import Path
        import sys

        if not Path(model_path).exists():
            print(f"❌ Model not found: {model_path}")
            sys.exit(1)

        if not Path(vectorizer_path).exists():
            print(f"❌ Vectorizer not found: {vectorizer_path}")
            sys.exit(1)

        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)


        self.attack_patterns = [
            r"\.\./",
            r"/etc/passwd",
            r"\bor\s+1\s*=\s*1\b",
            r"union\s+select",
            r"drop\s+table",
            r"<script",
            r"/admin",
            r"cmd=",
            r"exec\(",
        ]

    def check_rules(self, log_message):
        log_message = log_message.lower()

        for pattern in self.attack_patterns:
            if re.search(pattern, log_message):
                return True

        return False

    def predict(self, log_message):
        rule_match = self.check_rules(log_message)

        features = self.vectorizer.transform([log_message])
        prediction = self.model.predict(features)
        score = self.model.decision_function(features)[0]

        if rule_match:
            return "ANOMALY", score

        if prediction[0] == -1:
            return "ANOMALY", score

        return "NORMAL", score
