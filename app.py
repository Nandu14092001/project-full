from flask import Flask, render_template, request, send_file, flash
import os
import uuid
from converter import convert_to_pdf

app = Flask(__name__)
app.secret_key = "secret"
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "converted"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file:
            flash("No file uploaded")
            return render_template("index.html")

        ext = os.path.splitext(file.filename)[1]
        file_id = uuid.uuid4().hex
        input_path = os.path.join(UPLOAD_FOLDER, f"{file_id}{ext}")
        output_path = os.path.join(OUTPUT_FOLDER, f"{file_id}.pdf")
        file.save(input_path)

        try:
            convert_to_pdf(input_path, output_path)
        except Exception as e:
            flash(str(e))
            return render_template("index.html")

        return send_file(output_path, as_attachment=True)

    return render_template("index.html")