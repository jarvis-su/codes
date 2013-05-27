

import sqlite3

def getConnetion():
    return sqlite3.connect('D:/data/sqlite3/jtrac')

def getData(table_name):
    sql = 'select * from ' + table_name
    conn = getConnetion()
    cursor = conn.cursor()
    rec = cursor.execute(sql)
    result = rec.fetchall()
    for r in result:
        print(r);
    return result
    