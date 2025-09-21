---
id: dependencies#definition
title: "Functional Dependencies"
keywords: [FD, determinants, closures, composite keys]
jtbd: ["D1","D2","D3","D4","A1"]
---

## Definition
A functional dependency (FD) X → Y means that if two tuples agree on attributes X, they must also agree on attributes Y.  
- X = determinant  
- Y = dependent  
- An FD always applies inside a single relation.

## Checklist
- Determinants identified (LHS).  
- Dependents normalized to single attributes (RHS).  
- No cross-table dependencies.  
- Minimal cover derivable.  
- Candidate keys imply FD: key → all attributes.

## Pitfalls
- Confusing FD with multivalued dependency (MVD).  
- Keeping multiple attributes on RHS (must split).  
- Assuming FD between relations.  
- Using derived attributes in FD (e.g., age if birthdate stored).  

## Edge Cases
- **Trivial FD**: X → X is always true but useless.  
- **Composite determinants**: {course_code, semester} → grade. Must consider the entire set.  
- **False dependencies**: student_name → student_id is not valid (names are not unique).  
- **Redundant FDs**: if A → B and B → C, then A → C is implied and must be checked during minimal cover.  

## Mini-example
Relation: Enrollment(student_id, course_id, grade, semester)  
FDs:  
- {student_id, course_id, semester} → grade (composite determinant)  
- student_id → student_name (direct)  
- student_name → student_id (false, not guaranteed)
