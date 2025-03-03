#!/bin/bash
set -e  # Biar error langsung berhenti

# Update package list dan install Tesseract
apt-get update && apt-get install -y tesseract-ocr

# Cek apakah Tesseract sudah terpasang
which tesseract || echo "Tesseract tidak ditemukan setelah instalasi!" && exit 1

# Install semua dependencies dari requirements.txt
pip install --no-cache-dir -r requirements.txt

# Jalankan aplikasi dengan Gunicorn
gunicorn -w 4 -b 0.0.0.0:10000 app:app
