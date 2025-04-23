import time
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def connect_db():
    retry_attempts = 5
    for _ in range(retry_attempts):
        try:
            db = mysql.connector.connect(
                host="db",
                user="root",
                password="password",
                database="testdb"
            )
            return db
        except Error as e:
            print(f"Error: {e}, retrying...")
            time.sleep(5)  # Wait 5 seconds before retrying
    raise Exception("Could not connect to database after several attempts")

db = connect_db()
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
