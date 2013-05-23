import urllib.parse
import urllib.request
 
 #------------------------------需要修改1 begin---------------------------------
 #需要根据HttpFox插件修改 loginUrl,params.
loginUrl = 'http://kbserver/workflow/app/login/wicket:interface/%3A2%3Aform%3A%3AIFormSubmitListener%3A%3A/'
 #"登录成功"/"登录失败" 应修改为手动操作web登录成功/失败时的提示信息
successMsg = 'EPS Release Management'
failureMsg = ''
 #把所有需要自动登录的用户和密码写到这个数组中
accounts={'jsu':'sujiesujie'}
 #------------------------------需要修改1 start---------------------------------
 
 ###定义一个自动登录函数
def AutoLogin(user,password):
     try:
         req=urllib.request.Request(loginUrl)
         #------------------------------需要修改2 begin-----------------------------------
         req.add_header('Referer', 'http://kbserver/workflow/app/login/wicket:interface/%3A1%3Aform%3A%3AIFormSubmitListener%3A%3A/')
         req.add_header('User-agent', ' Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.64 Safari/537.31')
         req.add_header('Content-Type', 'application/x-www-form-urlencoded')
         req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
         req.add_header('Accept-Charset', 'GBK,utf-8;q=0.7,*;q=0.3')
         req.add_header('Accept-Encoding','gzip,deflate,sdch')
         params = urllib.parse.urlencode({'loginName': user,
                                          'password': password,
                                          'Submit': 'Submit'})    
         params = params.encode('ISO-8859-1')
         res = urllib.request.urlopen(req, params)
         html=res.read().decode('utf-8')
         #调试开关 可以查看登录成功后html页面中的关键字
         print(html)
         #------------------------------需要修改2 end-------------------------------------
         
         if html.find(failureMsg) != -1:
             return 'false'
         elif html.find(successMsg) != -1:
             return 'true'
     except EnvironmentError as err:
         return 'false'
     return 'false'
 
print('程序正在执行,如果一直没有响应请强制关闭......')
print()
 ### 遍历所有用户密码,调用自动登录函数
for obj in accounts:
     if (AutoLogin(obj,accounts[obj]) == 'false'):
         print ('%s: 登录-->失败.' % obj)
     else:
         print ('%s: 登录-->成功.' % obj)
print()
q=input("执行完毕,输入任意字符并按回车键退出程序:")