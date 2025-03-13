import pymysql
import os

from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

# 載入env資訊
load_dotenv()

# MySQL 連線設定
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# 連接 MySQL
def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

# 建立 users 資料表
def create_table():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(80) NOT NULL,
                email VARCHAR(120) NOT NULL UNIQUE
            );
        """)
    connection.commit()
    connection.close()

# API：取得所有使用者
@app.route("/users", methods=["GET"])
def get_users():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users;")
        users = cursor.fetchall()
    connection.close()
    return jsonify(users)

# API：新增使用者
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s);", (data["name"], data["email"]))
    connection.commit()
    connection.close()
    return jsonify({"message": "User added successfully!"}), 201

if __name__ == "__main__":
    create_table()  # 啟動時先建立資料表
    app.run(host="0.0.0.0", port=5000)
