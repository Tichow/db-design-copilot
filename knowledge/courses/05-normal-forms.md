---
id: normal-forms#overview
title: "Normal Forms"
keywords: [1NF, 2NF, 3NF, BCNF, 4NF, 5NF, normalization]
jtbd: ["N1","N2","N3","N4","N5","N6"]
---

## Definition
Normal forms are refinement rules applied to relational schemas to reduce redundancy and anomalies. Each higher form strengthens constraints on functional or multivalued dependencies.

## Checklist
- 1NF: All attributes atomic, no repeating groups.
- 2NF: No partial dependency of non-key attributes on part of a composite key.
- 3NF: No transitive dependency from non-key to non-key (with exceptions).
- BCNF: Every determinant must be a candidate key.
- 4NF: Remove nontrivial multivalued dependencies (MVD).
- 5NF: Remove join dependencies (JD) requiring further decomposition.

## Pitfalls
- Confusing 2NF with 3NF (partial vs transitive).
- Applying 3NF or BCNF without checking dependency preservation.
- Over-normalizing (loss of usability, performance costs).
- Forgetting that some transitive dependencies are allowed in 3NF if RHS is prime.
- Ignoring MVDs in 4NF (common in N–N associations with independent attributes).
- Overlooking JD in 5NF, especially in ternary relationships.

## Edge Cases
- **Partial dependency hidden**: relation Enrollment(student_id, course_id, student_name). Here student_name depends only on student_id, not the composite key.
- **3NF exception**: determinant is a superkey OR RHS is part of a candidate key.
- **BCNF vs dependency preservation**: decomposition may lose FD enforcement, requiring additional views or constraints.
- **4NF**: Student ↠ Language and Student ↠ Hobby imply decomposition, otherwise redundancy.
- **5NF**: Supplier–Part–Project relation may require decomposition if not all combinations are valid.

## Mini-example
Relation: Student(id, name, school_name, school_city)
FDs: id → name, school_name → school_city
- Violates 3NF: non-key attribute school_city depends transitively on id.
- Solution: split into Student(id, name, school_name) and School(school_name, school_city).
