import google.generativeai as genai

# Replace with your own API key
genai.configure(api_key="AQ.Ab8RN6J8EIAAPGLmY_wyQaiIZ6Ud6Xmi2fQtbSaO0uJVDTzy0A")

model = genai.GenerativeModel("gemini-2.5-flash")


def ai_explanation(url, prediction, confidence, risk):

    prompt = f"""
You are a cybersecurity expert.

Analyze this URL:

{url}

Prediction:
{prediction}

Confidence:
{confidence}%

Risk Level:
{risk}

Explain:

1. Why the URL was classified this way.
2. What risks the user should know.
3. Whether the user should continue or avoid the website.

Keep the answer under 120 words.
Use simple English.
"""

    response = model.generate_content(prompt)

    return response.text