from fastapi import APIRouter, Depends
from pydantic import BaseModel
import os, psycopg, httpx

from ..deps import get_conn
from .embeddings import embed_texts
from .prompts import AUGMENTED_PROMPT

TOP_K = int(os.getenv("TOP_K", "6"))

router = APIRouter()

class SearchReq(BaseModel):
    query: str
    k: int | None = None
    jtbd_hint: list[str] | None = None

class AskReq(BaseModel):
    query: str
    jtbd_hint: list[str] | None = None
    k: int | None = None

def _fetch_chunks(conn: psycopg.Connection, qvec, k, jtbd):
    with conn.cursor() as cur:
        if jtbd:
            cur.execute("""
                select doc_id, section, content,
                       1 - (embedding <=> %s::vector) as score
                from kb_chunks
                where jtbd_tags && %s::text[]
                order by embedding <=> %s::vector
                limit %s;
            """, (qvec, jtbd, qvec, k))
        else:
            cur.execute("""
                select doc_id, section, content,
                       1 - (embedding <=> %s::vector) as score
                from kb_chunks
                order by embedding <=> %s::vector
                limit %s;
            """, (qvec, qvec, k))
        rows = cur.fetchall()
    return [{"doc_id": r[0], "section": r[1], "content": r[2], "score": float(r[3])} for r in rows]

@router.post("/search")
async def search(req: SearchReq, conn=Depends(get_conn)):
    vec = (await embed_texts([req.query]))[0]
    k = req.k or TOP_K
    chunks = _fetch_chunks(conn, vec, k, req.jtbd_hint)
    return {"query": req.query, "chunks": chunks}

# Simple /ask that augments the prompt with retrieved chunks and calls an LLM
@router.post("/ask")
async def ask(req: AskReq, conn=Depends(get_conn)):
    qvec = (await embed_texts([req.query]))[0]
    k = req.k or TOP_K
    chunks = _fetch_chunks(conn, qvec, k, req.jtbd_hint)

    prompt = AUGMENTED_PROMPT.render(chunks=chunks, user_query=req.query)

    # call your LLM here (OpenAI shown as raw HTTP for clarity)
    llm_model = os.getenv("LLM_MODEL", "openai/gpt-5")
    key = os.getenv("OPENAI_API_KEY")
    headers = {"Authorization": f"Bearer {key}"}
    payload = {
        "model": llm_model,
        "messages": [
            {"role": "system", "content": "You are a careful assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.1
    }
    async with httpx.AsyncClient(timeout=120) as client:
        r = await client.post("https://api.openai.com/v1/chat/completions",
                              headers=headers, json=payload)
        r.raise_for_status()
        data = r.json()
        answer = data["choices"][0]["message"]["content"]

    return {
        "answer": answer,
        "used_chunks": [{"doc_id": c["doc_id"], "section": c["section"], "score": c["score"]} for c in chunks]
    }
