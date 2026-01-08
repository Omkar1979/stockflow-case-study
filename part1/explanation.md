### Part 1: Code Review & Debugging

### Issues Identified


1. No input validation / missing fields: The code assumes data exists and all keys are
present. Optional fields are not handled.

• Impact: Raises runtime errors (KeyError, TypeError). Bad client input can crash
the request.

3. SKU uniqueness not enforced: There is no check to ensure SKU is unique across the
platform.

• Impact: Duplicate SKUs break product identification, reporting, and integrations.

5. Product–warehouse modeling is incorrect: Product is created with a single warehouse id,
whereas business rules allow products in multiple warehouses.

• Impact: Prevents multi-warehouse inventory and leads to data duplication.

7. No transaction safety: Two separate commits are used.
8. 
• Impact: A product may be created without inventory if the second commit fails,
leading to an inconsistent database state.

9. Price precision issue: price is likely stored as a float.
10. 
• Impact: Floating-point precision errors in billing and reporting.
