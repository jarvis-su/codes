'''
Created on May 29, 2013

@author: C5023792
'''

import os   
import os.path   



if __name__ == '__main__':
    pass

def getTicketsList(fileName):
    list = []
    file = open(fileName,'r')
    try:
#         fileText = file.read()
        i = 0
        lines = file.readlines()
        for l in lines:
            s = l.replace('\n','')
            list+=[s]
#             print(s)
            i=i+1
#         while 1 :
#             line = file.readline()
#             if not line:
#                 break
#             list += [line]

    finally:
        file.close()
    return list

f = 'E:/temp/tickets.txt'
t = getTicketsList(f)
print(t)
for tt in t:
    print(tt)
