from src.alert import AlertManager

alert = AlertManager()

alert.send_alert(
    "GET /../../etc/passwd HTTP/1.1 404",
    -0.1852
)