import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port=3306,database='dbtestowa')

cursorObject = db.cursor()

tablequery = "CREATE TABLE IF NOT EXISTS student(firstname VARCHAR(50), lastname VARCHAR(50), studentid int)"
cursorObject.execute(tablequery)

insertsql = "INSERT INTO student(firstname,lastname,studentid) VALUES(%s,%s,%s)"
val = ("Jan","Nowak",4568)
cursorObject.execute(insertsql,val)
db.commit()
print(f"dodano rekordów {cursorObject.rowcount}")

values = [
    ("Anna","Kot",7545),
    ("Olga","Knot",756656),
    ("Henryk","Grum",7878),
    ("Nadia","Kos",9876),
    ("Marek","Ryć",12322),
    ("Benek","Bryk",65344),
    ("Feliks","Kot",5455),
]

cursorObject.executemany(insertsql,values)
db.commit()
print(f"dodano rekordów {cursorObject.rowcount}")
db.close()
