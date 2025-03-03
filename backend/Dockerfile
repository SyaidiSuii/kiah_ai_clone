# Gunakan imej rasmi Python sebagai asas
FROM python:3.11

# Pasang dependensi sistem yang diperlukan
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*

# Tetapkan direktori kerja dalam kontena
WORKDIR /app

# Salin fail projek ke dalam kontena
COPY . /app

# Pasang semua keperluan Python
RUN pip install --no-cache-dir -r requirements.txt

# Tetapkan command untuk run aplikasi Flask
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
