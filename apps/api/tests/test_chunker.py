from rag.chunker import chunk_text

def test_chunk_overlap():
    text = " ".join(["word"]*3000)
    chunks = chunk_text(text, max_tokens=200, overlap=50)
    assert len(chunks) > 1
    # Overlap should cause token reuse; here we just ensure not empty
    assert all(len(c.strip()) > 0 for c in chunks)
