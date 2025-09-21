from __future__ import annotations
from pathlib import Path
from typing import Iterator, Tuple, Dict, Any
import yaml, tiktoken, re

def split_front_matter(md_text: str) -> tuple[dict, str]:
    if md_text.startswith("---"):
        end = md_text.find("\n---", 3)
        if end != -1:
            fm = yaml.safe_load(md_text[3:end])
            body = md_text[end+4:]
            return fm or {}, body
    return {}, md_text

def strip_code_fences(text: str) -> str:
    # Optional: remove code blocks to avoid skewing retrieval for definitions
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)

def tokenize(text: str, enc_name: str = "cl100k_base"):
    enc = tiktoken.get_encoding(enc_name)
    return enc.encode(text), enc

def chunk_text(text: str, max_tokens=640, overlap=80, enc_name="cl100k_base") -> list[str]:
    toks, enc = tokenize(text, enc_name)
    chunks = []
    start = 0
    while start < len(toks):
        end = min(len(toks), start + max_tokens)
        chunk = enc.decode(toks[start:end])
        chunks.append(chunk.strip())
        if end == len(toks):
            break
        start = max(0, end - overlap)
    return [c for c in chunks if c]
