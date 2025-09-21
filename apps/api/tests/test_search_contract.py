from pydantic import BaseModel

class Chunk(BaseModel):
    doc_id: str
    section: str
    content: str
    score: float

def test_chunk_contract():
    c = Chunk(doc_id="normal-forms#3NF", section="Third Normal Form",
              content="A relation is in 3NF if ...", score=0.77)
    assert c.doc_id and c.section and c.content
    assert 0 <= c.score <= 1.0
