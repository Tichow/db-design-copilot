import os, httpx
from typing import List

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "openai/text-embedding-3-small")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

async def embed_texts(texts: List[str]) -> List[List[float]]:
    # Replace with your provider client; here using raw HTTP for clarity.
    # Batch requests if provider supports it. Keep per-chunk length reasonable.
    url = "https://api.openai.com/v1/embeddings"
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.post(url, headers=headers, json={
            "input": texts,
            "model": EMBEDDING_MODEL
        })
        resp.raise_for_status()
        data = resp.json()
        return [d["embedding"] for d in data["data"]]
