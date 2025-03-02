from flask import Flask, request, jsonify
from flask_cors import CORS
import pytesseract
from PIL import Image
import os
import shutil

# Tetapkan lokasi Tesseract
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Pastikan Tesseract bisa ditemukan
if shutil.which("tesseract") is None:
    pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

@app.route('/')
def home():
    return "Backend is running!"

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    try:
        image = request.files['image']
        img = Image.open(image)
        text = pytesseract.image_to_string(img)
        return jsonify({"extracted_text": text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Gunakan port yang disediakan Render
    app.run(host="0.0.0.0", port=port, debug=True)
