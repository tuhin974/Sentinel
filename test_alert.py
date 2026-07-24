from src.alert import send_slack_alert

sample = {
    "ip": "10.0.0.20",
    "method": "POST",
    "url": "/admin?query=DROP TABLE users",
    "status": 500,
    "timestamp": "24/Jul/2026:09:30:00"
}

status = send_slack_alert(sample)

print(status)