import os
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from pathlib import Path
import asyncio

from ..deps import get_conn
from .chunker import split_front_matter, strip_code_fences, chunk_text
from .embeddings import embed_texts
from .store import upsert_chunks

router = APIRouter()

class IngestConfig(BaseModel):
    glob: str = "knowledge/course/*.md"
    max_tokens: int = int(os.getenv("MAX_CHUNK_TOKENS", "640"))
    overlap: int = int(os.getenv("CHUNK_OVERLAP_TOKENS", "80"))

@router.post("/ingest")
async def ingest(cfg: IngestConfig, conn=Depends(get_conn)):
    files = sorted(Path(".").glob(cfg.glob))
    total = 0
    for p in files:
        md = p.read_text(encoding="utf-8")
        fm, body = split_front_matter(md)
        doc_id = fm.get("id", p.stem)
        section = fm.get("title", p.stem)
        jtbd = fm.get("jtbd", [])
        keywords = fm.get("keywords", [])
        clean = strip_code_fences(body)
        chunks = chunk_text(clean, cfg.max_tokens, cfg.overlap)
        embs = await embed_texts(chunks)
        rows = []
        for text, vec in zip(chunks, embs):
            rows.append((
                doc_id, section, jtbd, keywords, text, len(text.split()), vec
            ))
        upsert_chunks(conn, rows)
        total += len(rows)
    return {"ingested_files": len(files), "ingested_chunks": total}
