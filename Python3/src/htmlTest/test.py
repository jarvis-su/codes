'''
Created on May 20, 2013

@author: C5023792
'''


from bs4 import BeautifulSoup
import fileTest.readFile
import re

doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>']
soup = BeautifulSoup(''.join(doc))

print(soup.prettify())

if __name__ == '__main__':
    pass
print('ddddddddddd')
t = fileTest.readFile.getFileText('ddd')
print(t)