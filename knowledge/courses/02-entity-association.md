---
id: ea#modeling
title: "Entity-Association Modeling"
keywords: [EA, entities, associations, cardinalities, ternary, weak entity]
jtbd: ["M1","M2","M3","M4","R1","R2"]
---

## Definition
Entity-Association (EA) modeling represents a domain with:
- Entities: real-world objects, each with attributes.
- Associations: relationships between entities, with cardinalities.
- Attributes: properties describing entities or associations.
- Keys: unique identifiers for entities or associations.

## Checklist
- Entities identified with clear attributes.
- Each entity has a primary key (natural or surrogate).
- Associations annotated with cardinalities (1–1, 1–N, N–N).
- Ternary or higher-order associations modeled when needed.
- Associative entities introduced when N–N associations carry attributes.
- Weak entities supported by strong entities through identifying relationships.

## Pitfalls
- Treating an association attribute as if it belonged to an entity.
- Forgetting cardinalities, leading to ambiguous models.
- Omitting weak entities (e.g., Dependents of Employees) or their supporting keys.
- Forcing ternary associations into multiple binaries without justification.
- Using surrogate keys to replace natural relationship constraints without recording them.

## Edge Cases
- **Ternary associations**: Example: Student, Course, Semester. The grade depends on the triple (Student, Course, Semester). Splitting into binaries would lose information.
- **Weak entities**: Example: Dependent(name, birthdate) exists only with Employee(id). The PK is (employee_id, name).
- **Associative entities with attributes**: Example: Enrollment(student_id, course_id, grade). Grade belongs to the association, not to Student or Course.
- **Optional participation**: Example: A Company may have 0 or many Offers, but an Offer must always belong to exactly 1 Company (cardinality 0..N vs 1).

## Mini-example
Entities:  
- Student(id, name, email)  
- Course(code, title)  
- Semester(id, year)

Associations:  
- Enrollment(Student–Course, N–N) with attribute grade.  
- Registration(Student–Course–Semester, ternary, attribute exam_date).  

Resulting EA:  
- Entity: Student, Course, Semester  
- Associative entity: Enrollment(student_id, course_code, grade)  
- Ternary association: Registration(student_id, course_code, semester_id, exam_date)
