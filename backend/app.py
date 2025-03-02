from flask import Flask, request, jsonify
from flask_cors import CORS
import pytesseract
from PIL import Image

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def home():
    return "Backend is running!"

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    image = request.files['image']
    img = Image.open(image)
    text = pytesseract.image_to_string(img)

    return jsonify({"extracted_text": text})

if __name__ == '__main__':
    app.run(debug=True)
