---
id: glossary#basics
title: "Glossary & Principles"
keywords: [glossary, basics, definitions, database]
jtbd: ["S1","S2","M1"]
---

## Definition
This glossary defines the core vocabulary of database design used across all steps of the project (from idea to SQL).

## Glossary
- Entity: Real-world object represented in the system, modeled with attributes.
- Attribute: Property describing an entity; must be atomic (cannot be subdivided without loss of meaning).
- Relation: A table representing one entity or association; composed of tuples (rows) and attributes (columns).
- Tuple: A row in a relation, representing one occurrence of the entity or association.
- Primary key (PK): Minimal set of attributes uniquely identifying tuples in a relation.
- Candidate key: Any minimal key; one of them is chosen as the PK, others remain alternate keys.
- Surrogate key: Artificial key introduced when no stable natural key exists (e.g., UUID).
- Determinant: Left-hand side of a functional dependency (X in X → Y).
- Dependent: Right-hand side of a functional dependency (Y in X → Y).
- Superkey: A set of attributes that uniquely identifies tuples; may contain extra attributes.
- Foreign key (FK): Attribute in one relation that references the primary key of another.
- Business rule: Fact or constraint that must always hold in the modeled domain.
- Normal form: A refinement level of schema, defined by rules to reduce anomalies.

## Checklist
- All entities, attributes, relations, and constraints must be defined with these terms.
- Attributes must always be atomic.
- Candidate keys and superkeys are clearly distinguished.
- Surrogate keys are only introduced if natural keys are unstable.
- Every business rule must be expressible with constraints or associations.

## Pitfalls
- Confusing entity attributes with association attributes.
- Using synonyms inconsistently (relation vs table).
- Forgetting that every relation must have at least one candidate key.
- Introducing surrogate keys without preserving natural uniqueness.
- Confusing determinants with primary keys (a determinant may or may not be a key).

## Mini-example
Entity: Student(id, name, email)  
- Candidate keys: {id}, {email}  
- Chosen PK: id  
- Surrogate key: id (UUID) if emails are not stable over time  
Relation: STUDENT(id PK, name, email UQ)
