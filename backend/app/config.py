from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    app_name: str = "SitePulse"
    api_version: str = "v1"
    data_dir: str = os.getenv("SITEPULSE_DATA_DIR", "backend/data")
    chroma_dir: str = os.getenv("SITEPULSE_CHROMA_DIR", "backend/data/chroma")
    use_ollama: bool = os.getenv("SITEPULSE_USE_OLLAMA", "false").lower() == "true"
    ollama_url: str = os.getenv("OLLAMA_URL", "http://localhost:11434")
    ollama_model: str = os.getenv("OLLAMA_MODEL", "llama3.1:8b")


settings = Settings()
