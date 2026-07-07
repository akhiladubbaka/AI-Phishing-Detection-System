import re
import pandas as pd
from urllib.parse import urlparse
from scipy.sparse import hstack


SHORTENERS = [
    "bit.ly", "tinyurl.com", "goo.gl", "t.co", "ow.ly",
    "is.gd", "buff.ly", "adf.ly", "cutt.ly", "rebrand.ly"
]

def clean_url(url):
    url = url.lower().strip()
    url = re.sub(r"https?://", "", url)
    url = re.sub(r"www\.", "", url)
    return url

def extract_features(url):

    domain = urlparse("http://" + url).netloc

    features = {
        "url_length": len(url),
        "dot_count": url.count("."),
        "hyphen_count": url.count("-"),
        "underscore_count": url.count("_"),
        "slash_count": url.count("/"),
        "question_count": url.count("?"),
        "equal_count": url.count("="),
        "at_count": url.count("@"),
        "digit_count": sum(c.isdigit() for c in url),

        "has_https": int("https" in url),
        "has_www": int("www" in url),

        "has_ip": int(
            re.search(r"\d+\.\d+\.\d+\.\d+", url) is not None
        ),

        "contains_login": int("login" in url),
        "contains_verify": int("verify" in url),
        "contains_bank": int("bank" in url),
        "contains_secure": int("secure" in url),
        "contains_account": int("account" in url),
        "contains_update": int("update" in url),
        "contains_paypal": int("paypal" in url),
        "contains_signin": int("signin" in url),
        "contains_confirm": int("confirm" in url),
        "contains_password": int("password" in url),

        "is_shortened": int(
            any(short in url for short in SHORTENERS)
        ),

        "special_char_count":
            sum(not c.isalnum() for c in url),

        "domain_length": len(domain)
    }

    return pd.DataFrame([features])

def prepare_input(url, vectorizer):

    clean = clean_url(url)

    tfidf = vectorizer.transform([clean])

    manual = extract_features(clean)

    X = hstack([tfidf, manual.values])

    return X