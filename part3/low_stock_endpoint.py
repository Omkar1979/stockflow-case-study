@app.route('/api/companies/<int:company_id>/alerts/low-stock')
def low_stock_alerts(company_id):
    alerts = []

    inventories = (
        db.session.query(Inventory)
        .join(Product)
        .join(Warehouse)
        .filter(Warehouse.company_id == company_id)
        .all()
    )

    for inv in inventories:
        if not inv.product.has_recent_sales():
            continue

        threshold = inv.product.low_stock_threshold()
        if inv.quantity >= threshold:
            continue

        avg_daily_sales = inv.product.avg_daily_sales()
        days_left = int(inv.quantity / avg_daily_sales) if avg_daily_sales else None
        supplier = inv.product.primary_supplier()

        alerts.append({
            "product_id": inv.product.id,
            "product_name": inv.product.name,
            "sku": inv.product.sku,
            "warehouse_id": inv.warehouse.id,
            "warehouse_name": inv.warehouse.name,
            "current_stock": inv.quantity,
            "threshold": threshold,
            "days_until_stockout": days_left,
            "supplier": {
                "id": supplier.id,
                "name": supplier.name,
                "contact_email": supplier.contact_email
            } if supplier else None
        })

    return {"alerts": alerts, "total_alerts": len(alerts)}