'''
Created on May 23, 2013

@author: C5023792
'''
from bs4 import BeautifulSoup
import sqlite3

import htmlTest.LoginJtrac
import utils.dateUtil

def getPageInfoAndStore(Ticket_id, url, needLogin):
    user = 'jsu'
    pwd = 'sujiesujie'
    
    response = htmlTest.LoginJtrac.loginJtracAndGet(user, pwd, url, needLogin)
    
    # print(response)
    soup =BeautifulSoup(response)
    tables = soup.find_all(attrs={"class":"jtrac jtrac-view"});
    count = 0 
    conn = sqlite3.connect('D:/data/sqlite3/jtrac')
    c = conn.cursor()
    for table in tables:
    #     print(count)
        if count == 1:
            trs = table.find_all('tr')
            for tr in trs:
                tr_text = ''
                tds = tr.find_all('td')
                data = {}
                i = 0
                for td in tds:
                    tr_text = tr_text + td.text + ','
                    td_context = td.text
                    td_context = td_context.replace("\'"," ")
                    data[i] = td_context
                    i = i+1
                print(tr_text)
                if data.__len__()>0:
                    Logged_By = data[0]
                    Status = data[1]
                    Assigned_To = data[2]
                    Comment = data[3]
                    Time_Stamp = data[4]
                    t1 = utils.dateUtil.parseToDate(Time_Stamp) 
                    t2 = utils.dateUtil.convertToTianjin(t1)
                    TJ_datetime = utils.dateUtil.parseToString(t2)  
                    print('TJ_datetime==========' + TJ_datetime)                  
                    Ticket_Type = data[5]
                    Priority = data[6]
                    Urgency = data[7]
                    Impact = data[8]
                    Product = data[9]
                    State = data[10]
                    Program_Agency = data[11]
                    Component = data[12]
                    sql = "insert into info values('"+Ticket_id+"','"+Logged_By+"','"+Status+"','"+Assigned_To+"','"+Time_Stamp+"','"+ TJ_datetime+"','"+Comment+"','"+Ticket_Type+"','"+Priority+"','"+Urgency+"','"+Impact+"','"+Product+"','"+State+"','"+Program_Agency+"','"+Component+"')"
                    print(sql)
                    c.execute(sql)
                    conn.commit()
        count = count +1
    c.close()
