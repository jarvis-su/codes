'''
Created on May 21, 2013

@author: C5023792
'''
import webbrowser
import os 

import htmlTest.LoginJtrac
import DBOperation.sqliteOperation
import utils.fileUtil


if __name__ == '__main__':
    pass
print('hello')

# webbrowser.open('http://kbserver/workflow/app/')
# webbrowser.open('http://kbserver/workflow/app/item/TSGPRD-54897/')

# user = 'jsu'
# pwd = 'sujiesujie'
# url ='http://kbserver/workflow/app/item/TSGPRD-54897/'
# t = htmlTest.LoginJtrac.loginJtracAndGet(user, pwd, url)

# print(t)

# print(DBOperation.sqliteOperation.getAllData('t'))

t = {1,34,5}
print(len(t))
print(1<3)


f = 'E:/temp/tickets.txt'
t = utils.fileUtil.getTicketsList(f)
print(t)
for tt in t:
    print(tt)


