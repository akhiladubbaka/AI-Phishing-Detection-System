from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(
    filename,
    url,
    prediction,
    confidence,
    risk,
    reasons,
    ai_result
):

    styles = getSampleStyleSheet()

    pdf = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<b>AI Phishing Detection Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>URL:</b> {url}", styles["BodyText"]))

    story.append(Paragraph(f"<b>Prediction:</b> {prediction}", styles["BodyText"]))

    story.append(Paragraph(f"<b>Confidence:</b> {confidence}%", styles["BodyText"]))

    story.append(Paragraph(f"<b>Risk Level:</b> {risk}", styles["BodyText"]))

    story.append(Paragraph("<b>Reasons:</b>", styles["Heading2"]))

    for reason in reasons:
        story.append(Paragraph(f"• {reason}", styles["BodyText"]))

    story.append(Paragraph("<b>AI Analysis:</b>", styles["Heading2"]))

    story.append(Paragraph(ai_result, styles["BodyText"]))

    pdf.build(story)