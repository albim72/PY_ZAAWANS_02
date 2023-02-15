import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port=3306,database='dbtestowa')

cursorObject = db.cursor()

tablequery = "CREATE TABLE IF NOT EXISTS student(firstname VARCHAR(50), lastname VARCHAR(50), studentid int)"
cursorObject.execute(tablequery)

db.close()
