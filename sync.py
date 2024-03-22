import mysql.connector
import time



start = time.time()
conn = mysql.connector.connect(
    host="localhost",
    user="aref",
    password="EAsport1369",
    database="grafana"
)
with conn.cursor() as cursor:
    cursor.execute('SHOW TABLES')
    tables = cursor.fetchall()
    for t in tables:
        cursor.execute(f"select * from {t[0]}")
        data = cursor.fetchall()
        # print(data)
end = time.time()
print(end-start)