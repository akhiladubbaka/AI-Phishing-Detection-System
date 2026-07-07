from flask import Flask, render_template, request, send_file
import pickle
import os

from utils import prepare_input
from ai_explainer import explain_url
from gemini_ai import ai_explanation
from report_generator import generate_report
from database import create_table, save_prediction, get_history



app = Flask(__name__)

create_table()

last_report = {}

model = pickle.load(open("phishing_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

print("=" * 50)
print("Model expects:", model.n_features_in_)
print("Vectorizer vocabulary:", len(vectorizer.vocabulary_))
print("=" * 50)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    url = request.form["url"]

    X = prepare_input(url, vectorizer)
    

    print("Prepared Input Shape:", X.shape)

    prediction = model.predict(X)[0]

    score = model.decision_function(X)[0]

    confidence = min(abs(score) * 20, 100)
    confidence = round(confidence, 2)

    if prediction == 0:
        result = "⚠️ Phishing Website"
        risk = "High 🔴"
    else:
        result = "✅ Legitimate Website"
        risk = "Low 🟢"
    
    reasons = explain_url(url)
    
    ai_result = ai_explanation(
    url=url,
    prediction=result,
    confidence=confidence,
    risk=risk
)
    
    save_prediction(
    url,
    result,
    confidence,
    risk
)
    
    global last_report
    last_report = {
    "url": url,
    "prediction": result,
    "confidence": confidence,
    "risk": risk,
    "reasons": reasons,
    "ai_result": ai_result
}
    return render_template(
        "index.html",
        prediction=result,
        entered_url=url,
        confidence=confidence,
        risk=risk,
        reasons=reasons,
        ai_result=ai_result
    )
    
    

@app.route("/history")
def history():

    history_data = get_history()

    return render_template(
        "history.html",
        history=history_data
    )
    
    
@app.route("/download_report")
def download_report():

    filename = "AI_Phishing_Report.pdf"

    generate_report(
        filename=filename,
        url=last_report["url"],
        prediction=last_report["prediction"],
        confidence=last_report["confidence"],
        risk=last_report["risk"],
        reasons=last_report["reasons"],
        ai_result=last_report["ai_result"]
    )

    return send_file(
        filename,
        as_attachment=True
    )
if __name__ == "__main__":
    app.run(debug=True, port=5001)