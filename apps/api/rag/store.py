from typing import Sequence
import psycopg

INSERT_SQL = """
insert into kb_chunks (doc_id, section, jtbd_tags, keywords, content, token_count, embedding)
values (%s,%s,%s,%s,%s,%s,%s)
on conflict do nothing;
"""

def upsert_chunks(conn: psycopg.Connection, rows: Sequence[tuple]):
    with conn.cursor() as cur:
        for r in rows:
            cur.execute(INSERT_SQL, r)
