from flask import Flask, request, render_template
import mysql.connector
import os
import time

app = Flask(__name__)

#MySQLに接続する関数
def get_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME"),
        port=int(os.environ.get("DB_PORT"))
    )

#MySQLにテーブルがないときに自動作成するコード
def init_db():
    for i in range(5):
        try:
            conn=get_connection()
            cursor=conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                tel VARCHAR(255),
                address VARCHAR(255)
                )
            """)
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print("DB init failed, retrying...", e)
            time.sleep(2)

init_db()

#TOPページ
@app.route("/")
def index():
    return render_template("index.html")

#登録画面
@app.route("/register", methods=["GET"])
def register_form():
    return render_template("register.html")

#登録処理
@app.route("/register", methods=["POST"])
def register():
    username=request.form["username"]
    tel=request.form["tel"]
    address=request.form["address"]

    conn=get_connection()
    cursor=conn.cursor()

    
    query="""
        INSERT INTO users (username, tel, address) 
        VALUES (%s, %s, %s)

    """
    cursor.execute(query, (username, tel, address))
    conn.commit()


    #接続を閉じる
    cursor.close()
    conn.close()

    return "登録が完了しました"

#表示画面
@app.route("/display", methods=["GET"]) 
def display_form():
    return render_template("display.html")

#表示処理
@app.route("/display", methods=["POST"])
def display():
    users=None;
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("SELECT * FROM users")
    users=cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("display.html", users=users)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
    

