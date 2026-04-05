from flask import Flask, request, render_template, flash, url_for
import mysql.connector
import os
import time
import csv

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
    name=request.form["username"]
    tel=request.form["tel"]
    address=request.form["address"]

    conn=get_connection()
    cursor=conn.cursor()

    
    query="""
        INSERT INTO users (name, tel, address) 
        VALUES (%s, %s, %s)

    """
    cursor.execute(query, (name, tel, address))
    conn.commit()


    #接続を閉じる
    cursor.close()
    conn.close()

    flash("登録が完了しました")
    return redirect(url_for("/"))

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

#Search画面
@app.route("/search", methods=["GET"])
def search_form():
    return render_template("search.html")

#Search検索
@app.route("/search", methods=["POST"])
def search_data1():
    keyword1=request.form["keyword1"]
    keyword2=request.form["keyword2"]

    conn=get_connection()
    cursor=conn.cursor()

    query="""
	SELECT * FROM users 
	WHERE name LIKE %s AND address LIKE %s
	"""
    cursor.execute(query, 
	("%" + keyword1 + "%" if keyword1 else "%",
	"%" + keyword2 + "%" if keyword2 else "%"	
    ))
    users=cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("search.html", users=users)

#CSVアップロード画面
@app.route("/upload", methods=["GET"])
def upload_files():
    return render_template("upload.html")

#CSVアップロード処理
@app.route("/upload", methods=["POST"])
def upload():
    file=request.files["file"]
    if file.filename=="":
        return "ファイルが選択されていません"
    
    #CSVを読み込む
    csv_data=file.read().decode("utf-8").splitlines()
    reader=csv.reader(csv_data)

    conn=get_connection()
    cursor=conn.cursor()

    query="""
        INSERT INTO users(name, tel, address)
        VALUES (%s, %s, %s)
    """
    for row in reader:
        if len(row) < 3:
            continue 
        cursor.execute(query, (row[0],row[1],row[2]))
    
    conn.commit()
    cursor.close()
    conn.close()

    return "CSV の取り込みが完了しました"

#Delete画面
@app.route("/delete", methods=["GET"])
def delete_form():
    return render_template("delete.html")

#Delete検索
@app.route("/delete", methods=["POST"])
def delete_search():
    keyword=request.form["keyword"]

    conn=get_connection()
    cursor=conn.cursor()

    query="SELECT * FROM users WHERE name LIKE %s"
    cursor.execute(query, ("%" + keyword + "%",))
    users=cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("delete.html", users=users)

#Delete確認
@app.route("/delete_confirm", methods=["POST"])
def delete_confirm():
    user_id=request.form["id"]

    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()

    cursor.close()
    conn.close()

    return "削除が完了しました"

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
