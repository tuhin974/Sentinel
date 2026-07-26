# 🛡️ Sentinel – Real-Time Log Anomaly Detector

A real-time log monitoring and anomaly detection system developed during my internship at **Infyntrek Systèmes**.

Sentinel continuously monitors server log files, extracts meaningful features, applies Machine Learning and rule-based detection techniques, and immediately alerts administrators whenever suspicious activity is detected.

---

# ✨ Features

- 📄 Real-time log monitoring
- 🔍 Apache/Nginx log parsing
- ⚙️ Automatic feature extraction
- 🤖 Machine Learning anomaly detection
- 🛡️ Rule-based attack detection
- 📊 Confidence score prediction
- 🔔 Slack notification integration
- 📝 Professional logging
- ⚡ Live monitoring dashboard
- 🔒 Secure environment variable support (.env)

---

# 🏗️ System Architecture

```
                  ┌──────────────────┐
                  │   Server Logs    │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Real-Time Tailer │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │  Log Parser      │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Feature Extractor│
                  └────────┬─────────┘
                           │
            ┌──────────────┴──────────────┐
            ▼                             ▼
    Rule-Based Engine             Isolation Forest
            │                             │
            └──────────────┬──────────────┘
                           ▼
                  ┌──────────────────┐
                  │ Prediction Engine│
                  └────────┬─────────┘
                           │
           ┌───────────────┴───────────────┐
           ▼                               ▼
    Slack Notification             Live Dashboard
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
│   ├── normal_logs.csv
│   └── anomaly_logs.csv
│
├── docs/
│
├── logs/
│   └── sample.log
│
├── models/
│   ├── anomaly_detector.pkl
│   ├── vectorizer.pkl
│   └── model.pkl
│
├── screenshots/
│
├── src/
│   ├── alert.py
│   ├── config.py
│   ├── detector.py
│   ├── feature_extractor.py
│   ├── features.py
│   ├── logger.py
│   ├── parser.py
│   └── tailer.py
│
├── tests/
│
├── main.py
├── train.py
├── run_sentinel.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Technologies Used

- Python 3.x
- Scikit-learn
- Pandas
- NumPy
- Joblib
- Requests
- PyYAML
- python-dotenv

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/tuhin974/Sentinel.git
cd Sentinel
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
SLACK_WEBHOOK=https://hooks.slack.com/services/XXXXXXXX
```

---

# ⚙️ Configuration

Edit

```
config/config.yaml
```

Example

```yaml
log_file: logs/sample.log
```

---

# 🧠 Train the Model

Run

```bash
python train.py
```

This generates

```
models/anomaly_detector.pkl
models/vectorizer.pkl
```

---

# ▶️ Run Sentinel

```bash
python main.py
```

---

# 🧪 Sample Output

Normal Request

```
Prediction : ✅ NORMAL

Confidence : 78.2%
```

Anomaly

```
Prediction : 🚨 ANOMALY

Slack : Sent ✅

Confidence : 93.8%
```

---

# 📸 Screenshots

## Dashboard

Place screenshot here

```
screenshots/dashboard.png
```

---

## Slack Alert

Place screenshot here

```
screenshots/slack_alert.png
```

---

## Terminal Output

Place screenshot here

```
screenshots/terminal.png
```

---

# 🧪 Testing

Run

```bash
python test_alert.py
python test_detector.py
python test_pipeline.py
```

---

# 👨‍💻 Contributors

### Backend Development

**Tuhin Roy**

- Real-time monitoring
- Log parser
- Feature extraction
- Configuration
- Logging
- Slack Integration
- Dashboard
- Repository Management
- Git Integration

---

### Machine Learning Development

**Manish Gowda**

- Dataset preparation
- Isolation Forest training
- Model optimization
- Feature vectorization
- Detection pipeline

---

# 📈 Project Status

| Module | Status |
|---------|--------|
| Backend | ✅ Complete |
| Machine Learning | ✅ Complete |
| Dashboard | ✅ Complete |
| Slack Alerts | ✅ Complete |
| Logging | ✅ Complete |
| Testing | ✅ Complete |
| Integration | ✅ Complete |

---

# 📄 License

This project was developed as part of an internship at **Infyntrek Systèmes** for educational and learning purposes.

---

# ⭐ Acknowledgement

Special thanks to **Infyntrek Systèmes** for providing the opportunity to work on a real-world cybersecurity and machine learning project.