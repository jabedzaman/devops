from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="testdb"
)
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")

@app.route("/users", methods=["POST"])
def create_user():
    name = request.json["name"]
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    db.commit()
    return jsonify({"message": "User created"}), 201

@app.route("/users", methods=["GET"])
def list_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
