from flask import Flask, request, jsonify
import sqlite3
from db import init_db, get_all_orders, add_order

app = Flask(__name__)
init_db()

@app.route("/orders", methods=["GET", "POST"])
def orders():
    if request.method == "POST":
        data = request.get_json()
        add_order(data["user_id"], data["product_id"])
        return jsonify({"message": "Order placed"}), 201
    return jsonify(get_all_orders())

if __name__ == "__main__":
    app.run(port=5003)
