from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory catalog to store products
catalog = []

# Welcome message on root endpoint
@app.route('/')
def welcome():
    return "Welcome to the RESTful API!"

# GET /api/catalog - Returns a list of objects
@app.route('/api/catalog', methods=['GET'])
def get_catalog():
    return jsonify(catalog)

# POST /api/catalog - Save a product
@app.route('/api/catalog', methods=['POST'])
def add_product():
    product = request.get_json()
    if not product or 'name' not in product or 'price' not in product or 'category' not in product:
        return jsonify({"error": "Invalid product data. Must include 'name', 'price', and 'category'."}), 400
    catalog.append(product)
    return jsonify({"message": "Product added successfully!", "product": product}), 201

# GET /api/reports/total - Return the total value of the catalog
@app.route('/api/reports/total', methods=['GET'])
def get_total_value():
    total = sum(product['price'] for product in catalog)
    return jsonify({"total_value": total})

# GET /api/products/<category> - Returns products belonging to the given category
@app.route('/api/products/<category>', methods=['GET'])
def get_products_by_category(category):
    filtered_products = [product for product in catalog if product['category'].lower() == category.lower()]
    return jsonify(filtered_products)

if __name__ == '__main__':
    app.run(debug=True)