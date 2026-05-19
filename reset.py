import pymysql
import os

conn = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    port=int(os.getenv("DB_PORT"))
)

with conn.cursor() as cur:
    with open("reset.sql", "r") as f:
        sql = f.read()
        for statement in sql.split(";"):
            if statement.strip():
                cur.execute(statement)
conn.commit()
conn.close()
