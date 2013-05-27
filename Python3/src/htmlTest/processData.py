'''
Created on May 27, 2013

@author: C5023792
'''
import sqlite3
import htmlTest.processPageInfo

if __name__ == '__main__':
    pass

Ticket_id = 'TSGPRD-56019'
url ='http://kbserver/workflow/app/item/' + Ticket_id

conn = sqlite3.connect('D:/data/sqlite3/jtrac')

def clearExistedData(conn, ticket_id):
    sql = 'delete from info where trim(ticket_id) = \'' + ticket_id + '\'';
    print(sql)
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    c.close()



htmlTest.processPageInfo.getPageInfoAndStore(Ticket_id, url)
clearExistedData(conn, Ticket_id)