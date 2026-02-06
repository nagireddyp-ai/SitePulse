from datetime import datetime
from typing import Dict

from app.llm.ollama_client import OllamaClient


class KnowledgeGenerationAgent:
    def __init__(self, llm: OllamaClient) -> None:
        self.llm = llm

    def generate_article(self, incident: Dict, resolution: str) -> Dict:
        prompt = (
            "Create a concise knowledge-base article for IT engineers. "
            "Include title, symptoms, root cause, resolution, and verification steps.\n"
            f"Incident: {incident['title']}\n"
            f"Description: {incident['description']}\n"
            f"Resolution: {resolution}"
        )
        body = self.llm.generate(prompt)
        return {
            "id": f"kb-{incident['id']}",
            "title": f"KB: {incident['title']}",
            "content": body,
            "metadata": {
                "incident_id": incident["id"],
                "category": incident.get("category", "Linux"),
                "created_at": datetime.utcnow().isoformat(),
            },
        }
