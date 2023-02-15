import  sqlite3
from sqlite3 import Error
from conn import create_connection
from create_tables import cr

if __name__ == '__main__':
    #create_connection(r"C:\sqlite\db\pbaza.db")
    cr()
