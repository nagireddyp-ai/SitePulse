from typing import Dict, List

from app.llm.ollama_client import OllamaClient
from app.rag.vector_store import VectorStore


class RagChatAgent:
    def __init__(self, llm: OllamaClient, store: VectorStore) -> None:
        self.llm = llm
        self.store = store

    def answer(self, question: str) -> Dict:
        contexts = self.store.query(question)
        context_text = "\n\n".join([doc for doc, _ in contexts])
        prompt = (
            "You are an IT ops assistant. Answer using the context. "
            "If unsure, say you need more details.\n\n"
            f"Context:\n{context_text}\n\nQuestion: {question}"
        )
        response = self.llm.generate(prompt)
        sources: List[Dict] = [meta for _, meta in contexts]
        return {"answer": response, "sources": sources}
