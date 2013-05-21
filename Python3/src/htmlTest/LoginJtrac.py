import urllib.request  
import http.cookiejar  
import html.parser
import re  
import os  
import shutil  
filePath = "E:\\temp"  
      
if  os.path.isdir(filePath):  
        shutil.rmtree(filePath)  
elif os.path.isfile(filePath):  
        os.remove(filePath)  
os.makedirs(filePath)  
      
params = {"loginName3":"jsu", "password12":"Jarvis@2013"}  
webCookie = http.cookiejar.CookieJar()  
openner = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(webCookie))  
webRequest = openner.open("http://kbserver/workflow/app/login", urllib.parse.urlencode(params).encode()) 
print(webRequest.read) 
webRequest = openner.open("http://kbserver/workflow/app/item/TSGPRD-53803")  
htmlData = webRequest.read()  
print(htmlData)


