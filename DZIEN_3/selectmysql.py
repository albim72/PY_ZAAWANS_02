import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port=3306,database='dbtestowa')

cursorObject = db.cursor()

selquery = "SELECT firstname,lastname FROM student WHERE studentid > 9000"
cursorObject.execute(selquery)
wynik = cursorObject.fetchall()
for x,y in wynik:
    print(f"{x} {y}")

db.close()
