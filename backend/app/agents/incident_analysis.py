from typing import Dict

from app.llm.ollama_client import OllamaClient


class IncidentAnalysisAgent:
    def __init__(self, llm: OllamaClient) -> None:
        self.llm = llm

    def analyze(self, incident: Dict) -> Dict:
        prompt = (
            "You are an IT incident analyst. "
            "Classify severity (Low/Medium/High/Critical) and suggest next steps.\n"
            f"Incident: {incident['title']}\n"
            f"Description: {incident['description']}"
        )
        response = self.llm.generate(prompt)
        severity = self._infer_severity(incident)
        return {
            "severity": severity,
            "suggested_fix": response,
        }

    def _infer_severity(self, incident: Dict) -> str:
        priority = incident.get("priority", "P3")
        mapping = {"P1": "Critical", "P2": "High", "P3": "Medium", "P4": "Low"}
        return mapping.get(priority, "Medium")
