from flask import Flask, request, jsonify
import sqlite3
from db import init_db, get_all_users, add_user

app = Flask(__name__)
init_db()

@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "POST":
        data = request.get_json()
        add_user(data["name"])
        return jsonify({"message": "User added"}), 201
    return jsonify(get_all_users())

if __name__ == "__main__":
    app.run(port=5001)
