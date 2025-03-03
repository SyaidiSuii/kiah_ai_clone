import os
import pytesseract
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Cek lokasi Tesseract
possible_paths = [
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
]

tesseract_path = next((path for path in possible_paths if os.path.exists(path)), None)

if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
    print(f"Tesseract ditemukan di: {tesseract_path}")
else:
    print("⚠️ Tesseract tidak ditemukan!")

@app.route('/')
def home():
    return jsonify({
        "message": "Backend is running!",
        "tesseract_path": tesseract_path if tesseract_path else "Not Found"
    })

@app.route('/upload', methods=['POST'])
def upload():
    if not tesseract_path:
        return jsonify({"error": "Tesseract tidak ditemukan pada sistem ini"}), 500

    if 'image' not in request.files:
        return jsonify({"error": "Tidak ada file yang diunggah"}), 400

    try:
        image = request.files['image']
        filename = secure_filename(image.filename)
        img = Image.open(image).convert("L")  # Konversi ke grayscale
        extracted_text = pytesseract.image_to_string(img, config="--psm 6")  # Gunakan mode teks standar
        
        return jsonify({"extracted_text": extracted_text.strip()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
