from src.detector import LogDetector

detector = LogDetector()

logs = [
    "GET /home HTTP/1.1 200",
    "GET /products HTTP/1.1 200",
    "GET /../../etc/passwd HTTP/1.1 404",
    "GET /admin HTTP/1.1 403",
    "GET /index.php?id=' OR 1=1 -- HTTP/1.1 200"
]

for log in logs:
    label, score = detector.predict(log)
    print(f"{log} --> {label} (score={score:.4f})")