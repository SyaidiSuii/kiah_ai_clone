import os
import pytesseract
import subprocess
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Gunakan path Tesseract dari environment variable
tesseract_path = os.getenv("TESSERACT_PATH", "/usr/bin/tesseract")
pytesseract.pytesseract.tesseract_cmd = tesseract_path

@app.route('/')
def home():
    return jsonify({
        "message": "Backend is running!",
        "tesseract_path": tesseract_path if tesseract_path else "Not Found"
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
