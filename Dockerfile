FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV QDRANT_URL=http://localhost:6333
ENV PORT=5000
ENV OLLAMA_MODEL=llama3.2:3b
ENV OLLAMA_TEMPERATURE=0.7

WORKDIR /app

COPY backend/requirement.txt backend/requirement.txt
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libc6-dev \
    && pip install --no-cache-dir -r backend/requirement.txt \
    && apt-get purge -y --auto-remove gcc libc6-dev \
    && rm -rf /var/lib/apt/lists/*

COPY backend/ backend/
COPY frontend/ frontend/

WORKDIR /app/backend

EXPOSE 5000
CMD ["python", "app.py"]
