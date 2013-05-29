'''
Created on May 27, 2013

@author: C5023792
'''
import sqlite3
import htmlTest.processPageInfo

if __name__ == '__main__':
    pass

Ticket_id = 'TSGPRD-55055'
url ='http://kbserver/workflow/app/item/' + Ticket_id

conn = sqlite3.connect('D:/data/sqlite3/jtrac')

def isTicketExisted(conn, ticket_id):
    sql = 'select * from info where trim(ticket_id) = \'' + ticket_id + '\'';
    c = conn.cursor()
    res = c.execute(sql)
    length = len(res.fetchall())
    c.close()
    return length > 0
    

def clearExistedData(conn, ticket_id):
    sql = 'delete from info where trim(ticket_id) = \'' + ticket_id + '\'';
    print(sql)
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    c.close()

tickets = {'TSGPRD-56019','TSGPRD-54959','TSGPRD-53803','TSGPRD-55080','TSGPRD-55091','TSGPRD-55136','TSGPRD-55309','TSGPRD-55289','TSGPRD-45816','TSGPRD-55245','TSGPRD-55132','TSGPRD-55055','RELMGMTEPS-9418','RELMGMTEPS-9481','TSGPRD-55718','TSGPRD-55620','TSGPRD-55759','TSGPRD-55822','TSGPRD-56138'}
needLogin = True
for Ticket_id in tickets:
    url ='http://kbserver/workflow/app/item/' + Ticket_id
    if (isTicketExisted(conn, Ticket_id)):
        clearExistedData(conn, Ticket_id)
    htmlTest.processPageInfo.getPageInfoAndStore(Ticket_id, url, needLogin)
    needLogin = False


