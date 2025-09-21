import os
import psycopg
from psycopg_pool import ConnectionPool

POSTGRES_URL = os.getenv("POSTGRES_URL")

pool = ConnectionPool(
    conninfo=POSTGRES_URL,
    min_size=1,
    max_size=10,
    open=True,
)

def get_conn():
    with pool.connection() as conn:
        yield conn
