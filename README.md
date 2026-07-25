# 🛡️ Sentinel - Real-Time Log Anomaly Detector

A real-time log monitoring and anomaly detection system developed during my internship at **Infyntrek Systems**.

Sentinel continuously monitors application log files, extracts meaningful features, applies a Machine Learning model (Isolation Forest), detects anomalous activities, and instantly notifies the team through Slack.

---

# 📌 Project Overview

Modern applications generate thousands of log entries every minute, making manual monitoring inefficient and error-prone.

Sentinel automates this process by:

- Monitoring logs in real time
- Parsing Apache/Nginx log entries
- Extracting security-related features
- Detecting anomalies using Machine Learning
- Sending instant Slack alerts
- Maintaining professional log records
- Displaying a live monitoring dashboard

---

# ✨ Features

- ✅ Real-Time Log Monitoring
- ✅ Apache/Nginx Log Parsing
- ✅ Feature Extraction
- ✅ Isolation Forest Anomaly Detection
- ✅ Confidence Score
- ✅ Slack Alert Integration
- ✅ YAML Configuration
- ✅ Environment Variable Security (.env)
- ✅ Professional Logging
- ✅ Live Monitoring Dashboard
- ✅ Clean Terminal Interface

---

# 🏗️ System Architecture

```
                 Log File
                    │
                    ▼
             File Tailer Module
                    │
                    ▼
               Log Parser
                    │
                    ▼
          Feature Extraction
                    │
                    ▼
         Isolation Forest Model
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
      Normal Log         Anomaly Log
          │                   │
          ▼                   ▼
 Dashboard Update      Slack Notification
                        Log Recording
```

---

# 📂 Project Structure

```
Sentinel/
│
├── config/
│   └── config.yaml
│
├── data/
│   └── normal_logs.csv
│
├── docs/
│
├── logs/
│   └── sample.log
│
├── models/
│   └── model.pkl
│
├── screenshots/
│
├── src/
│   ├── alert.py
│   ├── config.py
│   ├── detector.py
│   ├── features.py
│   ├── logger.py
│   ├── parser.py
│   └── tailer.py
│
├── tests/
│   ├── test_alert.py
│   ├── test_config.py
│   ├── test_logger.py
│   ├── test_parser.py
│   └── test_tailer.py
│
├── .env
├── .gitignore
├── main.py
├── train.py
├── README.md
└── requirements.txt
```

---

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Pandas | Data Processing |
| Scikit-learn | Machine Learning |
| Isolation Forest | Anomaly Detection |
| Joblib | Model Persistence |
| Requests | Slack API Communication |
| PyYAML | Configuration Management |
| python-dotenv | Secure Environment Variables |

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/your-username/Sentinel.git

cd Sentinel
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔧 Configuration

Update

```
config/config.yaml
```

Example

```yaml
log_file: logs/sample.log
model_path: models/model.pkl
log_level: INFO
```

Create a `.env` file

```
SLACK_WEBHOOK=YOUR_SLACK_WEBHOOK_URL
```

---

# ▶️ Running the Project

Train the Model

```bash
python train.py
```

Start Sentinel

```bash
python main.py
```

---

# 📊 Sample Output

```
============================================================
🛡️ Sentinel - Real-Time Log Anomaly Detector
============================================================

IP Address : 10.0.0.20
Method     : POST
URL        : /admin?query=DROP TABLE users
Status     : 500

Prediction
--------------------
Score      : -0.0334
Confidence : 93.3%

Prediction : 🚨 ANOMALY

Slack      : Sent ✅
```

---

# 📈 Dashboard

Sentinel continuously displays

- Processed Logs
- Normal Requests
- Anomalies
- Slack Alerts
- System Uptime

---

# 🔔 Slack Integration

Whenever an anomaly is detected:

- A Slack notification is sent instantly.
- The event is recorded in the application log.
- The dashboard statistics are updated.

---

# 🔍 Testing

Run test modules

```bash
python tests/test_parser.py

python tests/test_config.py

python tests/test_logger.py

python tests/test_alert.py
```

---

# 🔐 Security

- Slack Webhook stored using `.env`
- Configuration separated using YAML
- Runtime logs ignored from Git
- Secrets excluded using `.gitignore`

---

# 📸 Screenshots

Screenshots will be available in:

```
screenshots/
```

- Dashboard
- Slack Alert
- Normal Request
- Anomaly Detection

---

# 🚀 Future Improvements

- Web Dashboard
- Docker Deployment
- Email Alerts
- Multiple ML Models
- REST API
- Cloud Deployment
- Grafana Integration

---

# 👨‍💻 Internship Project

This project was developed during my internship at **Infyntrek Systems** as a real-world backend and machine learning integration project focused on real-time log anomaly detection.

---

# 📄 License

This project is intended for educational and internship demonstration purposes.

---

# ⭐ Acknowledgement

Special thanks to **Infyntrek Systems** for providing the opportunity to work on a real-world cybersecurity and machine learning project that strengthened my skills in Python development, backend engineering, and ML integration.