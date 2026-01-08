### Part 2: Database Design



**Proposed Schema (PostgreSQL-style)**
1 Company ( id , name )
2 Warehouse ( id , company_id , name , location )
3 Product ( id , company_id , name , sku UNIQUE , price DECIMAL (10 ,2) ,
product_type )
4 Inventory ( id , product_id , warehouse_id , quantity )
5 InventoryMovement ( id , inventory_id , change_qty , reason , created_at )
6 Supplier ( id , name , contact_email )
7 ProductSupplier ( product_id , supplier_id , lead_time_days )
8 ProductBundle ( parent_product_id , child_product_id , quantity )




**Relationshi**^^
• Company - Warehouses (1:N)
• Product - Warehouse (M:N via Inventory)
• Inventory - InventoryMovement (1:N)
• Product - Supplier (M:N)
• Product - Product (Bundles)




 **Indexes & Constraints**
• sku UNIQUE
• (product id, warehouse id) UNIQUE on Inventory
• Index on Inventory.quantity
• Index on InventoryMovement.created at
Design Justification
• Inventory separated from Product enables multi-warehouse scaling.
• InventoryMovement allows a full audit trail.
• Bundle table supports recursive product composition.



**Missing Requirements / Questions for Product Team**
• Can SKUs be reused across companies?
• Are bundles sellable independently?
• Do inventory movements include reservations?
• How is sales activity defined?
• Do suppliers differ per warehouse?
• Are negative inventories allowed?
