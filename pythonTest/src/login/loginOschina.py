import urllib.request as http#instead of urllib2
import urllib.parse #urlencode is used
import http.cookiejar as cookie
'''
Created on May 17, 2013

@author: C5023792
'''
#target url
url = 'http://kbserver/workflow/app/item/TSGPRD-55822'
#login url
orig_url='http://kbserver/workflow/app/login'
domain='kbserver'

myCookie = http.HTTPCookieProcessor(cookie.CookieJar())
opener = http.build_opener(myCookie)

post_data = {'loginName':'jsu',
        'password':'Jarvis@2013',
        'origURL': orig_url,
        'domain': domain}

data=urllib.parse.urlencode(post_data)
data=data.encode(encoding='utf-8') # data should be encoded.
req=http.Request(url,data)
rsp_html_src=opener.open(req).read()
print(rsp_html_src)

#write response html to a .html file
file = open("d:/homepage.html", "wb")
file.write(rsp_html_src)