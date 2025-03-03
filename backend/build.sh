#!/bin/bash
apt-get update && apt-get install -y tesseract-ocr
pip install -r requirements.txt
gunicorn -w 4 -b 0.0.0.0:10000 app:app
