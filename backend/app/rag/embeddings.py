import hashlib
from typing import List


def embed_text(text: str) -> List[float]:
    """Generate a lightweight deterministic embedding for offline use."""
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    chunks = [digest[i : i + 8] for i in range(0, len(digest), 8)]
    return [int(chunk, 16) % 1000 / 1000 for chunk in chunks]
