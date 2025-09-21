---
id: matrices#overview
title: "DF Matrices & Interpreted Matrices"
keywords: [DF matrix, interpreted matrix, transitive, multivalued]
jtbd: ["A3","A4"]
---

## Definition
A **DF matrix** is a tabular view of functional dependencies:  
- Rows = determinants  
- Columns = dependents  
- Cell ✓ if determinant → dependent is in minimal cover.

An **interpreted matrix** enriches the DF matrix by classifying the type of dependency:  
- ✓ direct (present in minimal cover)  
- T transitive (implied through a chain)  
- M multivalued dependency  

## Checklist
- DF matrix lists all FDs from minimal cover.  
- Determinants normalized (alphabetical, single RHS).  
- Interpreted matrix matches classifications (✓, T, M).  
- Both matrices available in CSV and human-readable form.  

## Pitfalls
- Forgetting candidate keys as determinant rows.  
- Mislabeling a transitive dependency as direct.  
- Omitting MVDs from interpreted matrix.  
- Adding cross-table dependencies (not valid).  

## Edge Cases
- **Composite determinant**: row labeled {A,B} must appear explicitly.  
- **Empty determinant**: ∅ → A (rare, usually modeling error).  
- **Dense matrix**: too many ✓, indicates possible redundancy.  
- **MVDs**: only appear in interpreted matrix, never in plain DF matrix.  

## Mini-example
Relation: Course(code, prof, room)  
FDs:  
- code → prof  
- prof → room  
Matrix:  
- Row {code}: prof ✓  
- Row {prof}: room ✓  
Interpreted:  
- code → prof = ✓ (direct)  
- prof → room = ✓ (direct)  
- code → room = T (transitive)
