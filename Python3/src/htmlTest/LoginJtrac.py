import urllib.request  
import http.cookiejar  

loginUrl = 'http://kbserver/workflow/app/login/wicket:interface/%3A2%3Aform%3A%3AIFormSubmitListener%3A%3A/'

def loginJtrac(user, pwd):
    req=urllib.request.Request(loginUrl)
         #------------------------------需要修改2 begin-----------------------------------
    req.add_header('Referer', 'http://kbserver/workflow/app/login/wicket:interface/%3A1%3Aform%3A%3AIFormSubmitListener%3A%3A/')
    req.add_header('User-agent', ' Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.64 Safari/537.31')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    req.add_header('Accept-Charset', 'GBK,utf-8;q=0.7,*;q=0.3')
    req.add_header('Accept-Encoding','gzip,deflate,sdch')
    params = urllib.parse.urlencode({'loginName': user,
                                     'password': pwd,
                                     'Submit': 'Submit'})    
    params = params.encode('ISO-8859-1')
    res = urllib.request.urlopen(req, params)
    html=res.read().decode('utf-8')
         #调试开关 可以查看登录成功后html页面中的关键字
#     print(html)
    
    #设置cookie  
cookie = http.cookiejar.CookieJar() 
cookieProc = urllib.request.HTTPCookieProcessor(cookie) 
opener = urllib.request.build_opener(cookieProc) 
urllib.request.install_opener(opener)
  

def loginJtracAndGet(user, pwd, url, needLogin):
    if(needLogin):
        loginJtrac(user, pwd)
    res1 = urllib.request.urlopen(url)
    html1=res1.read().decode('utf-8')
    return html1
