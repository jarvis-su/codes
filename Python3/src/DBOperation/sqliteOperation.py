

import sqlite3

def getConnetion():
    return sqlite3.connect('D:/data/sqlite3/jtrac')

def getConn(database):
    return sqlite3.connect(database)

def getAllData(table_name):
    sql = 'select * from ' + table_name
    conn = getConnetion()
    cursor = conn.cursor()
    rec = cursor.execute(sql)
    result = rec.fetchall()
    for r in result:
        print(r);
    return result

def getAllDataBySql(sql):
    conn = getConnetion()
    cursor = conn.cursor()
    rec = cursor.execute(sql)
    result = rec.fetchall()
    for r in result:
        print(r);
    return result
    