'''
Created on May 23, 2013

@author: C5023792
'''
from bs4 import BeautifulSoup

import htmlTest.LoginJtrac


if __name__ == '__main__':
    pass

user = 'jsu'
pwd = 'sujiesujie'
url ='http://kbserver/workflow/app/item/TSGPRD-54897/'
response = htmlTest.LoginJtrac.loginJtracAndGet(user, pwd, url)

# print(response)
soup =BeautifulSoup(response)
tables = soup.find_all(attrs={"class":"jtrac jtrac-view"});
count = 0 
for table in tables:
#   print(table)
  print(count)
  if count == 1:
#     print(table)
    trs = table.find_all('tr')
    for tr in trs:
#         print(tr)
        tr_text = ''
        tds = tr.find_all('td')
        data = {}
        i = 0
        for td in tds:
#             print(td.text)
            tr_text = tr_text + td.text + ','
            data[i] = td.text
            i = i+1
        print(tr_text)
        
        
  count = count +1
