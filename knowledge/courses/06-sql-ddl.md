---
id: sql#ddl
title: "SQL DDL (Postgres)"
keywords: [SQL, DDL, PK, FK, UQ, CK, NN, indexes, views]
jtbd: ["Q1","Q2","Q3","E1"]
---

## Definition
SQL Data Definition Language (DDL) defines and manages relational schemas, constraints, indexes, and views.

## Checklist
- Primary key defined with NOT NULL.
- Foreign keys reference valid PKs.
- Unique constraints enforce business uniqueness.
- Check constraints ensure rule compliance.
- Indexes created for PKs, UQs, and FKs.
- Views used for reporting or simplifying queries.

## Pitfalls
- Forgetting to index foreign keys, leading to slow joins.
- Using surrogate keys without preserving natural uniqueness.
- Overusing indexes on low-cardinality attributes (boolean, gender).
- Embedding business logic in views instead of schema constraints.
- Creating redundant indexes (UQ already provides an index).

## Edge Cases
- **Composite primary keys**: `PRIMARY KEY(student_id, course_id)`. Requires careful FK referencing.
- **Self-referencing FKs**: Employee(manager_id) REFERENCES Employee(id).
- **Deferrable constraints**: useful when order of insertion is uncertain.
- **Check constraints**: must be deterministic and simple (no subqueries).
- **Views**: should not contain non-deterministic functions if reproducibility is required.
- **RLS (Row-Level Security)**: must be explicitly enabled, not part of DDL but critical for Supabase.

## Mini-example
create table student (
  id uuid primary key,
  email varchar(255) unique not null,
  age int check (age >= 18)
);

create table enrollment (
  student_id uuid references student(id),
  course_id uuid,
  primary key(student_id, course_id)
);

create view student_summary as
select id, email from student;

