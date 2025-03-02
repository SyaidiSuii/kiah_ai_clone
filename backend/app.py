import os
import pytesseract
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import sys

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Coba beberapa kemungkinan lokasi Tesseract
possible_paths = [
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
    # Tambahkan lokasi lain jika diperlukan
]
try:
    print(pytesseract.get_tesseract_version())
except Exception as e:
    print(f"Error: {e}")

tesseract_path = None
for path in possible_paths:
    if os.path.exists(path):
        tesseract_path = path
        break

if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
    print(f"Tesseract found at: {tesseract_path}")
else:
    print("Tesseract not found in any of the expected locations!")

@app.route('/')
def home():
    if tesseract_path:
        return f"Backend is running! Tesseract found at: {tesseract_path}"
    else:
        return "Backend is running, but Tesseract not found!"

@app.route('/upload', methods=['POST'])
def upload():
    if not tesseract_path:
        return jsonify({"error": "Tesseract not found on this system"}), 500
        
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
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)