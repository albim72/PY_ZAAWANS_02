import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-K4JE02F;DATABASE=autokomis;Trusted_Connection=yes')

curor = conn.cursor()
curor.execute("SELECT @@version;")
tu = curor.fetchall()

print(tu)
