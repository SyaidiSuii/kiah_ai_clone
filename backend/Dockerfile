# Gunakan imej rasmi Python sebagai asas
FROM python:3.11-slim

# Pasang dependensi sistem yang diperlukan untuk Tesseract OCR
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*

# Tetapkan direktori kerja dalam container
WORKDIR /app

# Salin fail projek ke dalam container
COPY . .

# Pasang semua keperluan Python
RUN pip install --no-cache-dir -r requirements.txt

# Tetapkan PORT default dalam container
ENV PORT=5000

# Jalankan aplikasi Flask menggunakan Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
