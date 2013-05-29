'''
Created on May 29, 2013

@author: C5023792
'''
from datetime import * 
import datetime  
import time

if __name__ == '__main__':
    pass

# today = datetime.date.today()  
# yesterday = today - datetime.timedelta(days = 1)  
# tomorrow = today + datetime.timedelta(days = 1)  
#   
# print(yesterday, today, tomorrow)  

def parseToDate(dateStr):
    jtracDateFomat ='%Y-%m-%d %H:%M:%S'
    t = datetime.datetime.strptime(dateStr,jtracDateFomat)
    return t

def convertToTianjin(jtracDatetime):
    delta = 13 # hours
    tj = jtracDatetime + datetime.timedelta(hours=delta)
    return tj

def isHolidayOrWeekEnd(date):
    
    return False

def calculateNonWorkingHours(beginDate, endDate):
    nonWork = 0
    return nonWork

test ='2013-05-14 20:06:22'
t1 = parseToDate(test)
print(t1)
t2 = convertToTianjin(t1)
print(t2)

dt = datetime.datetime.now()
print ('(%Y-%m-%d %H:%M:%S %f):', dt.strftime('%Y-%m-%d %H:%M:%S %f'))
print ('(%Y-%m-%d %H:%M:%S %p):', dt.strftime('%y-%m-%d %I:%M:%S %p'))
print ('%%a: %s ' % dt.strftime('%a'))
print ('%%A: %s ' % dt.strftime('%A'))
print ('%%b: %s ' % dt.strftime('%b'))
print ('%%B: %s ' % dt.strftime('%B'))
print ('日期时间%%c: %s ' % dt.strftime('%c'))
print ('日期%%x：%s ' % dt.strftime('%x'))
print ('时间%%X：%s ' % dt.strftime('%X'))
print ('今天是这周的第%s天 ' % dt.strftime('%w'))
print ('今天是今年的第%s天 ' % dt.strftime('%j'))
print ('今周是今年的第%s周 ' % dt.strftime('%U'))
