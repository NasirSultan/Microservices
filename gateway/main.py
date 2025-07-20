from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "POST":
        return requests.post("http://localhost:5001/users", json=request.json).json()
    return requests.get("http://localhost:5001/users").json()

@app.route("/products", methods=["GET", "POST"])
def products():
    if request.method == "POST":
        return requests.post("http://localhost:5002/products", json=request.json).json()
    return requests.get("http://localhost:5002/products").json()

@app.route("/orders", methods=["GET", "POST"])
def orders():
    if request.method == "POST":
        return requests.post("http://localhost:5003/orders", json=request.json).json()
    return requests.get("http://localhost:5003/orders").json()

if __name__ == "__main__":
    app.run(port=5000)
