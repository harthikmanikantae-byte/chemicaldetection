import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
import io

def export_to_csv(df):
    """
    Converts dataframe to CSV string for download.
    """
    return df.to_csv(index=False).encode('utf-8')

def export_to_pdf(papers, drug_name):
    """
    Generates a PDF summary of research papers using ReportLab.
    """
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Custom Title Style
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=20,
        alignment=1 # Center
    )
    
    content = []
    
    # Title
    content.append(Paragraph(f"Literature Summary: {drug_name}", title_style))
    content.append(Spacer(1, 12))
    
    # Intro
    content.append(Paragraph(f"This document provides a summary of recent research papers related to the electrochemical detection of {drug_name}.", styles['Normal']))
    content.append(Spacer(1, 20))
    
    # Papers
    for paper in papers:
        content.append(Paragraph(f"<b>Title:</b> {paper['title']}", styles['Heading3']))
        content.append(Paragraph(f"<b>Authors:</b> {paper['authors']}", styles['Normal']))
        content.append(Paragraph(f"<b>Journal:</b> {paper['journal']} ({paper['year']})", styles['Normal']))
        content.append(Paragraph(f"<b>DOI:</b> {paper['doi']}", styles['Normal']))
        content.append(Spacer(1, 10))
        content.append(Paragraph("<b>Abstract:</b>", styles['Normal']))
        content.append(Paragraph(paper['abstract'], styles['Normal']))
        content.append(Spacer(1, 20))
        content.append(Paragraph("-" * 80, styles['Normal']))
        content.append(Spacer(1, 20))
    
    doc.build(content)
    pdf_bytes = buffer.getvalue()
    buffer.close()
    return pdf_bytes
