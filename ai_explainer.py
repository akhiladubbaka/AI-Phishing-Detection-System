from urllib.parse import urlparse

def explain_url(url):

    reasons = []

    url_lower = url.lower()

    if len(url) > 75:
        reasons.append("URL is unusually long.")

    if url.count(".") > 3:
        reasons.append("URL contains many subdomains.")

    if "@" in url:
        reasons.append("URL contains '@', which is often used to mislead users.")

    if any(word in url_lower for word in ["login", "verify", "secure", "account",
                                          "update", "confirm", "password", "paypal"]):
        reasons.append("Sensitive keywords are present in the URL.")

    if sum(not c.isalnum() for c in url) > 10:
        reasons.append("URL contains many special characters.")

    domain = urlparse("http://" + url_lower).netloc

    if domain.replace(".", "").isdigit():
        reasons.append("An IP address is used instead of a domain name.")

    if not reasons:
        reasons.append("No major phishing indicators were detected.")

    return reasons