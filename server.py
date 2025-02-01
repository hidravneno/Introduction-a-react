from flask import Flask, request, render_template
import json
from http import HTTPStatus 
from config import get_db

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from flask"

# @app.post("/")
# @app.put("/")
# @app.patch("/")

@app.get("/test")
def test():
    return "this is another endpoint"

# This is a JSON implementation
@app.get("/api/about")
def about():
    name={"name":"Eduardo"}
    return json.dumps(name)

@app.get("/about-me")
def about_me():
    user_name = "Eduardo"
    return render_template("about-me.html", name=user_name)

products = []

def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

# GET all products
@app.get("/api/products")
def get_products():
    products_db = []
    cursor = db.products.find({})
    for product in cursor:
        print("product ", product)
        products_db.append(product)
    return json.dumps(products_db), HTTPStatus.OK

# POST a product
@app.post("/api/products")
def save_product():
    product = request.get_json()
    print(f"Product: {product}")
    products.append(product)
    return "Product saved"

@app.delete("/api/products/<int:index>")
def delete_product(index):
    if 0 <= index < len(products):
        deleted_product = products.pop(index)
        print(f"Deleted product: {deleted_product}")
        return "Product deleted"

app.run(debug=True)
