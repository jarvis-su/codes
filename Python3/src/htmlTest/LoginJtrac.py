#      Python 模拟登录,然后记录cookie,之后获取公司OA主页公文信息  
import urllib.request  
import http.cookiejar  
import html.parser
import re  
import os  
import shutil  
#      公文HTML下载目录  
filePath = "E:\\temp"  
      
    # 初始化文件目录  
if  os.path.isdir(filePath):  
        shutil.rmtree(filePath)  
elif os.path.isfile(filePath):  
        os.remove(filePath)  
os.makedirs(filePath)  
      
# 登录并获取最新的公文列表  
params = {"loginName3":"jsu", "password12":"Jarvis@2013"}  
webCookie = http.cookiejar.CookieJar()  
openner = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(webCookie))  
webRequest = openner.open("http://kbserver/workflow/app/login", urllib.parse.urlencode(params).encode())  
webRequest = openner.open("http://kbserver/workflow/app/item/TSGPRD-53803")  
htmlData = webRequest.read()  
print(htmlData)
  
# # map,用于记录首页的公文URL  
# OApages = {}  
# # 解析HTML,HTMLParser为系统默认的解析方式,HTML文件具有容错性,所以最好不使用xml解析  
# # 解析公文首页的公文列表  
# class MyHtmlParser(HTMLParser):  
#     _a_Flag = False  
#     _a_title = ""  
#     def handle_starttag(self, tag, attrs):  
#         if tag == "a":  # 解析公文相关的URL  
#             for pageUrl in attrs:  
#                 if pageUrl[0] == 'href':  
#                     self._a_Flag = True  
#                     self._a_URL = pageUrl[1]  
#                     self._a_URL = self._a_URL.replace("javascript:openwin('", "http://192.168.8.109/")  
#                     self._a_URL = self._a_URL.replace("');", "")  
#     def handle_data(self, data):  
#         if self._a_Flag :  
#             self._a_title = self. _a_title + data  
#     def handle_endtag(self, tag):  
#         if tag == "a":  
#             self._a_title = re.sub("\W", "", self._a_title)  
#             OApages[self._a_URL] = self._a_title  
#             self._a_title = ""  
#             self._a_Flag = False  
#               
# MyHtmlParser().feed(htmlData)  
#   
# # 转码URL中的中文字符串  
# def encoderForUrl(strURL):  
#     # 0 将非特殊字符串替换掉  
#     _tempStr = re.sub("[a-z\d&/:.?=]+", ";", strURL)  
#     # 1 获取中文字符串  
#     _tempStrArr = _tempStr.split(";")  
#     # 2用中文转码后的字符串替换中文字符串  
#     for _tempStrValue in _tempStrArr:  
#         strURL = strURL.replace(_tempStrValue, urllib.parse.quote(_tempStrValue))  
#     return strURL  
#   
# # 下载公文内容  
# print("公文首面共", len(OApages), "条公文")  
# for url, title in OApages.items():  
#     url = encoderForUrl(url)  # 这里的URL里面的参数抱括中文,例如name=小胖子,直接使用会出错,所以要将其转码  
#     webRequest = openner.open(url)  
#     htmlData = webRequest.read().decode('gbk')  
#     dataFile = open(filePath + os.sep + title + ".html", "w")  
#     dataFile.write(htmlData)  
#     print("写入公文:", title, "成功")  


