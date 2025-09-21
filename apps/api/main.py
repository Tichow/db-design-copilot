import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

from .rag.ingest import router as ingest_router
from .rag.search import router as search_router

load_dotenv()

app = FastAPI(title="DB-Design Copilot — RAG API")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(ingest_router, prefix="/rag", tags=["rag"])
app.include_router(search_router, prefix="/rag", tags=["rag"])
