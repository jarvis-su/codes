'''
Created on May 29, 2013

@author: C5023792
'''

import os   
import os.path   



if __name__ == '__main__':
    pass

def getTicketsList(fileName):
    list = {}
    file = open(fileName,'r')
    try:
        fileText = file.read()
#         lines = fileText.readlines()
        for l in fileText:
            list.append(l)
    finally:
        file.close()
    return list

f = 'E:/temp/tickets.txt'
t = getTicketsList(f)
print(t)
