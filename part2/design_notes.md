## Part 2: Database Design

### Proposed Schema (PostgreSQL-style)

1. Company ( id, name )
2. Warehouse ( id, company_id, name, location )
3. Product ( id, company_id, name, sku UNIQUE, price DECIMAL(10,2), product_type )
4. Inventory ( id, product_id, warehouse_id, quantity )
5. InventoryMovement ( id, inventory_id, change_qty, reason, created_at )
6. Supplier ( id, name, contact_email )
7. ProductSupplier ( product_id, supplier_id, lead_time_days )
8. ProductBundle ( parent_product_id, child_product_id, quantity )

### Relationships

Company — Warehouses: (1:N)

Product — Warehouse: (M:N via Inventory)

Inventory — InventoryMovement: (1:N)

Product — Supplier: (M:N)

Product — Product: (Bundles)

### Indexes & Constraints

sku UNIQUE

(product_id, warehouse_id) UNIQUE on Inventory

Index on Inventory.quantity

Index on InventoryMovement.created_at

### Design Justification

Multi-Warehouse Scaling: Inventory separated from Product enables tracking across multiple locations.

Audit Trail: InventoryMovement allows a full historical record of stock changes.

Recursive Composition: Bundle table supports complex product compositions (products made of other products).

### Missing Requirements / Questions for Product Team

Can SKUs be reused across companies?

Are bundles sellable independently?

Do inventory movements include reservations?

How is sales activity defined?

Do suppliers differ per warehouse?

Are negative inventories allowed?
