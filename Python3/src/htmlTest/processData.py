'''
Created on May 27, 2013

@author: C5023792
'''
import htmlTest.processPageInfo

if __name__ == '__main__':
    pass

Ticket_id = 'TSGPRD-56019'
url ='http://kbserver/workflow/app/item/' + Ticket_id

htmlTest.processPageInfo.getPageInfoAndStore(Ticket_id, url)
