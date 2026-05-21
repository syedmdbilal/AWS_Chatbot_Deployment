from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer
from langchain_qdrant import QdrantVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
import threading

from config import QDRANT_URL, OLLAMA_MODEL, OLLAMA_TEMPERATURE

print("🌿 Initializing LushBot Models...")

# Qdrant client
client = QdrantClient(QDRANT_URL)

# Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# LLM
llm = OllamaLLM(model=OLLAMA_MODEL, temperature=OLLAMA_TEMPERATURE)

# 🔥 RAG VECTORSTORE (Your CSV data!)
vectorstore = QdrantVectorStore(
    client=client,
    collection_name="my_vectors",
    embedding=embeddings
)

# Thread lock
log_lock = threading.Lock()

# Initialize collections
def init_db():
    # Main data collection
    if not client.collection_exists("my_vectors"):
        client.create_collection(
            "my_vectors",
            vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE)
        )
        print("✅ Created my_vectors")
    
    # Chat logs
    if not client.collection_exists("chat_logs"):
        client.create_collection(
            "chat_logs",
            vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE)
        )
        print("✅ Created chat_logs")

init_db()
print("✅ All models ready!")
