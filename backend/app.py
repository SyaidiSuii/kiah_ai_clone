import os
import pytesseract
import subprocess
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Cek apakah berjalan di Render
if os.getenv("RENDER"):
    tesseract_path = "/usr/bin/tesseract"  # Path default di Linux
else:
    possible_paths = [
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
    ]
    tesseract_path = next((path for path in possible_paths if os.path.exists(path)), None)

# Pastikan Tesseract bisa dipanggil
try:
    if tesseract_path:
        pytesseract.pytesseract.tesseract_cmd = tesseract_path
        test_output = subprocess.check_output([tesseract_path, "--version"], stderr=subprocess.STDOUT)
        print(f"Tesseract ditemukan: {test_output.decode().strip()}")
    else:
        raise FileNotFoundError("Tesseract tidak ditemukan!")
except Exception as e:
    print(f"⚠️ Error: {e}")
    tesseract_path = None

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
