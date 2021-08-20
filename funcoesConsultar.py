import pyodbc

def consultar01(conn):
    cursor = conn.cursor()
    cursor.execute("select * from cliente")
    for i in cursor:
        print(f'linha = {i}')
    return 0

def consultar01():
    return 0

def consultar01():
    return 0

def consultar01():
    return 0

def consultar01():
    return 0