from typing import Dict, List, Tuple

import chromadb

from app.config import settings
from app.rag.embeddings import embed_text


class VectorStore:
    def __init__(self) -> None:
        self.client = chromadb.PersistentClient(path=settings.chroma_dir)
        self.collection = self.client.get_or_create_collection("sitepulse_kb")

    def upsert_documents(self, documents: List[Dict]) -> None:
        ids = [doc["id"] for doc in documents]
        texts = [doc["content"] for doc in documents]
        embeddings = [embed_text(text) for text in texts]
        metadatas = [doc.get("metadata", {}) for doc in documents]
        self.collection.upsert(
            ids=ids,
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas,
        )

    def query(self, query: str, top_k: int = 3) -> List[Tuple[str, Dict]]:
        embedding = embed_text(query)
        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
        )
        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        return list(zip(documents, metadatas))
