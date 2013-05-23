'''
Created on May 23, 2013

@author: C5023792
'''
import sqlite3

if __name__ == '__main__':
    pass

conn = sqlite3.connect('D:/data/sqlite3/jtrac')
c = conn.cursor()
c.execute("insert into t values (3,'jarvis')")
conn.commit()
rec = c.execute("select * from t")
print(c.fetchall())