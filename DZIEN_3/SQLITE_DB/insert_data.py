import sqlite3
from sqlite3 import Error
from conn import create_connection

def create_project(conn,project):
    sql = """
    INSERT INTO projects(name,begin_date,end_date) VALUES(?,?,?)
    """

    cur = conn.cursor()
    cur.execute(sql,project)
    conn.commit()
    return cur.lastrowid


def create_task(conn, task):
    sql = """
    INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date) VALUES(?,?,?,?,?,?)
    """

    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

def insert():
    database = r"C:\sqlite\db\pbaza.db"
    conn = create_connection(database)
    
    with conn:
        project1 = ('Super Apka -> Python Analiza Danych','2023-01-02','2023-10-10')
        project_id_1 = create_project(conn,project1)

        project2 = ('Sieć neuronowa -> Python', '2023-03-12', '2024-01-12')
        project_id_2 = create_project(conn, project2)
        
        task_11 = ("Analiza wymagań dotyczących aplikacji",1,1,project_id_1,'2023-01-04','2023-02-27')
        task_12 = ("Przygotowanie diagramów UML",2,1,project_id_1,'2023-02-15','2023-04-08')

        task_21 = ("Analiza wymagań dotyczących aplikacji", 1, 1, project_id_2, '2023-03-15', '2023-05-10')
        task_22 = ("Przygotowanie dmodelu sieci neuronowej", 3, 1, project_id_2, '2023-04-30', '2023-07-02')
        
        create_task(conn,task_11)
        create_task(conn,task_12)
        create_task(conn,task_21)
        create_task(conn,task_22)
        
        
    
