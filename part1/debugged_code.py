from decimal import Decimal
from sqlalchemy.exc import IntegrityError

@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()

    if not data or 'name' not in data or 'sku' not in data:
        return {"error": "Missing required fields"}, 400

    if Product.query.filter_by(sku=data['sku']).first():
        return {"error": "SKU already exists"}, 409

    warehouse = Warehouse.query.get(data.get('warehouse_id'))
    if not warehouse:
        return {"error": "Invalid warehouse"}, 400

    try:
        product = Product(
            name=data['name'],
            sku=data['sku'],
            price=Decimal(str(data.get('price', 0)))
        )

        inventory = Inventory(
            product=product,
            warehouse=warehouse,
            quantity=data.get('initial_quantity', 0)
        )

        db.session.add_all([product, inventory])
        db.session.commit()

    except IntegrityError:
        db.session.rollback()
        return {"error": "Database error"}, 500

    return {"message": "Product created", "product_id": product.id}, 201