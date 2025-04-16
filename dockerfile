FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive

# Instalando pacotes do sistema
RUN apt-get update && \
    apt-get install -y tesseract-ocr \
                       poppler-utils \
                       libgl1 \
                       libsm6 libxext6 libxrender-dev \
                       tesseract-ocr-por && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Diretório de trabalho no container
WORKDIR /app

# Copia o requirements primeiro
COPY requirements.txt .

# Instala as libs Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos
COPY . .

CMD ["python", "app.py"]
