from sklearn.feature_extraction.text import TfidfVectorizer
import joblib


class FeatureExtractor:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def fit_transform(self, messages):
        """
        Learn vocabulary from training logs
        and convert them into TF-IDF vectors.
        """
        return self.vectorizer.fit_transform(messages)

    def transform(self, messages):
        """
        Convert new log messages into
        TF-IDF vectors using existing vocabulary.
        """
        return self.vectorizer.transform(messages)

    def save(self, path):
        """
        Save trained vectorizer.
        """
        joblib.dump(self.vectorizer, path)

    def load(self, path):
        """
        Load trained vectorizer.
        """
        self.vectorizer = joblib.load(path)