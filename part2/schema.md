### schema 

```
Company(id, name)
Warehouse(id, company_id, name, location)
Product(id, company_id, name, sku UNIQUE, price DECIMAL(10,2), product_type)
Inventory(id, product_id, warehouse_id, quantity)
InventoryMovement(id, inventory_id, change_qty, reason, created_at)
Supplier(id, name, contact_email)
ProductSupplier(product_id, supplier_id, lead_time_days)
ProductBundle(parent_product_id, child_product_id, quantity)
```