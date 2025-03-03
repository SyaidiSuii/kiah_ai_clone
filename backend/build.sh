#!/bin/bash
apt-get update && apt-get install -y tesseract-ocr
pip install --no-cache-dir -r requirements.txt
