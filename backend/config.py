import hashlib
import os

QDRANT_URL = os.environ.get("QDRANT_URL", "http://localhost:6333")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2:3b")
OLLAMA_TEMPERATURE = float(os.environ.get("OLLAMA_TEMPERATURE", "0.7"))
PORT = int(os.environ.get("PORT", "5000"))
SECRET_KEY = os.environ.get("SECRET_KEY", "lushbot-secret-key-2026-change-this")
ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "lushbot2026")
ADMIN_USERS = {
    ADMIN_USERNAME: hashlib.sha256(ADMIN_PASSWORD.encode()).hexdigest()
}
