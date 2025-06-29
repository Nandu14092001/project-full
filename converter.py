from PIL import Image
from fpdf import FPDF
from docx2pdf import convert as docx_convert
import os

def convert_to_pdf(input_path, output_path):
    ext = os.path.splitext(input_path)[1].lower()

    if ext in ['.jpg', '.jpeg', '.png']:
        image = Image.open(input_path).convert("RGB")
        image.save(output_path)
    elif ext == '.txt':
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        with open(input_path, 'r', encoding='utf-8') as file:
            for line in file:
                pdf.cell(200, 10, txt=line.strip(), ln=1)
        pdf.output(output_path)
    elif ext == '.docx':
        docx_convert(input_path, output_path)
    else:
        raise Exception("Unsupported file type for PDF conversion.")