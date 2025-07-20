from flask import Flask, request, jsonify
import sqlite3
from db import init_db, add_product, get_all_products

app = Flask(__name__)
init_db()

@app.route("/products", methods=["GET", "POST"])
def products():
    if request.method == "POST":
        data = request.get_json()
        add_product(data["title"])
        return jsonify({"message": "Product added"}), 201
    return jsonify(get_all_products())

if __name__ == "__main__":
    app.run(port=5002)
