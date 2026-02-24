from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def generate_report(filename, summary_text):

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("AI Network Intelligence Report", styles['Title']))
    elements.append(Spacer(1, 0.5 * inch))
    elements.append(Paragraph(summary_text, styles['Normal']))

    doc.build(elements)