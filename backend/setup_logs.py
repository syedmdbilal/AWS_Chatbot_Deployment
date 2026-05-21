from qdrant_client import QdrantClient, models

from config import QDRANT_URL

client = QdrantClient(QDRANT_URL)

# Create logs collection
try:
    client.create_collection(
        collection_name="chat_logs",
        vectors_config=models.VectorParams(
            size=384,  # Same as sentence-transformers model
            distance=models.Distance.COSINE
        )
    )
    print(" Created 'chat_logs' collection in Qdrant")
except Exception as e:
    print(f"Collection already exists or error: {e}")
