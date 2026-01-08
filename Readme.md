# StockFlow Backend Case Study – Solution

This repository contains my complete solution for the **Inventory Management System for B2B SaaS (StockFlow)** backend case study, submitted as part of the internship application process.


All explanations, assumptions, and design decisions are documented clearly.

---

## 📂 Repository Structure

stockflow-backend-case-study/
│
├── README.md
│
├── part1/
│ ├── debugged_code.py
│ └── explanation.md
│
├── part2/
│ ├── schema.md
│ └── design_notes.md
│
├── part3/
│ ├── low_stock_endpoint.py
│ └── explanation.md



Each folder corresponds directly to a section of the case study.

---

## 🧩 Part 1: Code Review & Debugging

**Folder:** `part1_code_review/`

### Objective
Review an existing API endpoint for creating products and inventory, identify issues, explain their production impact, and provide a corrected version.

---

### Issues Identified

1. **No input validation / missing fields**
   - The code assumes request data exists and all required keys are present.
   - Optional fields are not handled.

   **Impact:**  
   - Causes runtime errors such as `KeyError` and `TypeError`.
   - A single bad client request can crash the API.

2. **SKU uniqueness not enforced**
   - No check to ensure SKU is unique across the platform.

   **Impact:**  
   - Duplicate SKUs break product identification, reporting, and integrations.

3. **Incorrect product–warehouse modeling**
   - Product is created with a single `warehouse_id`.
   - Business rules allow products to exist in multiple warehouses.

   **Impact:**  
   - Prevents multi-warehouse inventory support.
   - Leads to data duplication and incorrect stock reporting.

4. **No transaction safety**
   - Product and inventory are committed in separate transactions.

   **Impact:**  
   - Product may be created without inventory if the second commit fails.
   - Results in inconsistent database state.

5. **Price precision issue**
   - Price is likely stored as a floating-point value.

   **Impact:**  
   - Floating-point precision errors affect billing and financial reports.

---

### Corrected Implementation

The corrected and fully commented implementation is available in:

part1_code_review/debugged_code.py



Key improvements:
- Input validation
- SKU uniqueness enforcement
- Proper warehouse validation
- Atomic database transactions
- Safe handling of monetary values using `Decimal`
- Graceful error handling using `IntegrityError`

---

## 🗄️ Part 2: Database Design

**Folder:** `part2_database_design/`

### Objective
Design a scalable and flexible database schema based on incomplete requirements.

---

### Proposed Schema (PostgreSQL-style)

Company(id, name)

Warehouse(id, company_id, name, location)

Product(id, company_id, name, sku UNIQUE, price DECIMAL(10,2), product_type)

Inventory(id, product_id, warehouse_id, quantity)

InventoryMovement(id, inventory_id, change_qty, reason, created_at)

Supplier(id, name, contact_email)

ProductSupplier(product_id, supplier_id, lead_time_days)

ProductBundle(parent_product_id, child_product_id, quantity)



This schema is documented in:
part2_database_design/schema.md


---

### Key Design Decisions

- Products are independent of warehouses.
- Inventory acts as a join table between products and warehouses.
- Inventory movements provide a complete audit trail.
- Product bundles support composite products.
- Suppliers are linked through a many-to-many relationship.

Detailed explanations are available in:
part2_database_design/design_notes.md



---

### Missing Requirements Identified

Questions raised for the product team include:
- Are SKUs unique globally or per company?
- Can bundles be sold independently?
- Do inventory movements include reservations?
- How is “recent sales activity” defined?
- Can inventory go negative?

---

## 🚨 Part 3: Low-Stock Alerts API

**Folder:** `part3_low_stock_api/`

### Objective
Implement an API endpoint that returns low-stock alerts for a company while handling real-world business constraints.

---

### Endpoint Specification

GET /api/companies/{company_id}/alerts/low-stock


---

### Business Rules Implemented

- Low-stock threshold varies by product type
- Alerts are generated only for products with recent sales activity
- Multiple warehouses per company are supported
- Supplier information is included for reordering
- Days until stockout is estimated using average daily sales

---

### Edge Cases Handled

- Products with no recent sales are ignored
- Zero sales velocity avoids division errors
- Missing supplier data is handled safely
- Supports large datasets conceptually

---

### Implementation

The implementation with clear comments and documented assumptions is available in:

part3_low_stock_api/low_stock_endpoint.py



Additional assumptions are documented in:
part3_low_stock_api/assumptions.md


---

## 📝 Assumptions

Due to intentionally incomplete requirements, assumptions were made and clearly documented in each part.

No assumptions beyond those explicitly stated in the solution were introduced.

---

## 🛠️ Technologies Referenced

- Python
- Flask
- SQLAlchemy
- PostgreSQL (conceptual schema design)

This repository focuses on **design, correctness, and reasoning**, not on building a fully runnable production application.

---

## 🎯 Purpose of This Repository

This repository demonstrates:
- Backend debugging and problem-solving ability
- Database design thinking
- API design and edge-case handling
- Clear communication of technical decisions

---

## 📎 Submission Note

This repository is submitted as the **Case Study Solution Repository URL** as required in the internship application.

---

## 🙏 Thank You
