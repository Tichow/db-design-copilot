create extension if not exists vector;
create extension if not exists pgcrypto;

create table if not exists kb_chunks (
  id uuid primary key default gen_random_uuid(),
  doc_id text not null,          -- e.g. "normal-forms#3NF"
  section text not null,         -- e.g. "3. Third Normal Form"
  jtbd_tags text[] not null,     -- e.g. '{N3,A4}'
  keywords text[] not null,      -- e.g. '{3NF,transitive}'
  content text not null,
  token_count int not null,
  embedding vector(1536) not null, -- adjust to your embedding model size
  created_at timestamptz default now()
);

create index if not exists idx_kb_chunks_vec on kb_chunks
using ivfflat (embedding vector_cosine_ops) with (lists = 100);

create index if not exists idx_kb_chunks_doc on kb_chunks (doc_id);
create index if not exists idx_kb_chunks_jtbd on kb_chunks using gin (jtbd_tags);
