import urllib.request  
import http.cookiejar  
import html.parser
import re  
import os  
import shutil  

# Can not connection base on the network of Xerox office
# proxy_handler = urllib.request.ProxyHandler({'http':'10.237.80.138:8080'})  
# proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()  
# opener = urllib.request.build_opener(urllib.request.HTTPHandler, proxy_handler) 
# f = opener.open('http://www.baidu.com') 
# a = f.read()
# print(a)

req = urllib.request.Request('http://python.org/')
response = urllib.request.urlopen(req)
the_page = response.read()
#print(the_page)

# Can not connection base on the network of Xerox Office
# proxy_support = urllib.request.ProxyHandler({'http':'10.237.80.138:8080'})  
# opener = urllib.request.build_opener(proxy_support)
# urllib.request.install_opener(opener)
# a = urllib.request.urlopen("http://python.org/").read()
# print(a)



params = {"username":"admin", "pwd":"111111"}  
webCookie = http.cookiejar.CookieJar()  
openner = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(webCookie))  
webRequest = openner.open("http://10.237.89.207:8888/survey/login.jsp", urllib.parse.urlencode(params).encode()) 
print(webRequest.read) 
webRequest = openner.open("http://10.237.89.207:8888/survey/admin/SurveyEdit.jsp?sid=35")  
htmlData = webRequest.read()  
print(htmlData)