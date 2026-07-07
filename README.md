# 🛡️ AI Phishing Detection System

An AI-powered web application that detects whether a website URL is **Legitimate** or **Phishing** using Machine Learning and Google Gemini AI.

## 🚀 Live Demo

https://ai-phishing-detection-system-dh6b.onrender.com

---

## 📌 Features

- 🔍 Detects Phishing URLs using Machine Learning
- 🤖 AI explanation using Google Gemini
- 📊 Confidence Score
- 🚨 Risk Level Prediction
- 📝 Feature-based explanation
- 📄 Download PDF Report
- 🗄️ Prediction History (SQLite Database)
- 🌐 Deployed on Render

---

## 🛠️ Tech Stack

### Frontend
- HTML
- CSS

### Backend
- Flask
- Python

### Machine Learning
- Scikit-learn
- TF-IDF Vectorizer
- LinearSVC

### AI
- Google Gemini API

### Database
- SQLite

### Deployment
- Render
- GitHub

---

## 📂 Project Structure

```
AI_Phishing_project/
│
├── app.py
├── utils.py
├── database.py
├── gemini_ai.py
├── ai_explainer.py
├── report_generator.py
│
├── phishing_model.pkl
├── tfidf_vectorizer.pkl
│
├── templates/
│     └── index.html
│
├── static/
│     └── style.css
│
├── requirements.txt
├── Procfile
├── .python-version
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/akhiladubbaka/AI-Phishing-Detection-System.git
```

Move into the project folder

```bash
cd AI-Phishing-Detection-System
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Linux / macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open

```
http://127.0.0.1:5001
```

---

## 🔑 Environment Variable

Create your Gemini API Key and set it as an environment variable.

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

## 📊 Machine Learning Model

- TF-IDF Vectorizer
- LinearSVC Classifier

The model predicts whether a URL is:

- ✅ Legitimate Website
- ⚠️ Phishing Website

---

## 📄 Report Generation

The application generates a downloadable PDF report containing:

- URL
- Prediction
- Confidence Score
- Risk Level
- Feature-based Explanation
- AI Explanation

---

## 🗄️ Database

SQLite is used to store:

- URL
- Prediction
- Confidence
- Risk Level
- Timestamp

---

## 🌐 Deployment

The application is deployed on Render.

Live URL:

https://ai-phishing-detection-system-dh6b.onrender.com

---

## 👩‍💻 Author

**Akhila Dubbaka**

GitHub:
https://github.com/akhiladubbaka

---

## 📜 License

This project is developed for educational and learning purposes.
