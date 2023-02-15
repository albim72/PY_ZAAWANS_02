import sqlite3
from sqlite3 import Error
from conn import create_connection

def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()
    for row in rows:
        print(row)


def select_all_projects(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM projects")

    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_task_by_priority(conn,priority):
    cur  = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority = ?",(priority,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

def select():
    database = r"C:\sqlite\db\pbaza.db"
    conn = create_connection(database)

    with conn:
        print("1. Zadanie z filtrem po priorytecie")
        prio = input("Podaj priorytet zadania: ")
        select_task_by_priority(conn,prio)

        print("1. Wsztystkie zadania: ")
        select_all_tasks(conn)
