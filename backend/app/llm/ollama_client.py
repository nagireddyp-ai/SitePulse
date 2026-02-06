import requests

from app.config import settings


class OllamaClient:
    def __init__(self) -> None:
        self.base_url = settings.ollama_url
        self.model = settings.ollama_model
        self.use_ollama = settings.use_ollama

    def generate(self, prompt: str) -> str:
        if not self.use_ollama:
            return "".join(
                [
                    "Proposed steps: ",
                    "1) Identify recent changes. ",
                    "2) Validate configuration. ",
                    "3) Apply fix and monitor.",
                ]
            )
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={"model": self.model, "prompt": prompt, "stream": False},
            timeout=30,
        )
        response.raise_for_status()
        return response.json().get("response", "")
