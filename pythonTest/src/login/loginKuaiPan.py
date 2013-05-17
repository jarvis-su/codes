import urllib.request 
import json

#登录金山快盘
class Login_kp:
    def __init__(self):  #初始化函数
        # 获得一个opener
        # py2x 版本 HTTPCookieProcessor() 要传入一个cookiejar实例
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
        #装载一个opener
        urllib.request.install_opener(self.opener)

    
    def login(self, username, password): #登录
        print('请等待，正在登陆中..........')
        
        # proxy setting
#         proxy_support = urllib.request.ProxyHandler({'http': '10.237.80.137:8080'})
#         opener = urllib.request.build_opener(proxy_support)
#         urllib.request.install_opener(opener)
        #end proxy setting

        # 快盘的登录地址
        url = 'https://www.kuaipan.cn/index.php?ac=account&op=login'
        #定义post数据，账号和密码,封装成 ?username=username&userpwd=userpwd
        data = urllib.parse.urlencode({'username':username, 'userpwd':password})
        print('username = ' + username)
        print('password = ' + password)
        #必须把封装的数据转换
        data = data.encode('ISO-8859-1')

        try:
            #这里利用urlopen 进行请求提交，获得一个reponse
            # 也可以利用这种方式   rp = self.opener.open(url, data)
            response = urllib.request.urlopen(url, data)
            #读取获得的返回数据
            rp_data = response.read()
            #对返回的数据进行字符转换，要不会乱码
            rp_data = rp_data.decode('utf-8', 'ignore')
            
        except Exception as e:     # 在py2  except Exception , e  注意 as
            print('网络连接错误')
            print(str(e))
            return False
            
            #假如登录成功，页面数据会有<span class="ico ico-share">这个标签，如果没有，就代表登录失败
        if rp_data.find('<span class="ico ico-share">') == -1:
            print('用户名或者密码错误')
            return False
            
        print('%s 登录成功，请执行相关操作' % username)
        return True
            
    
    def logout(self):
        url = 'http://www.kuaipan.cn/index.php?ac=account&op=logout'
        rp = urllib.request.urlopen(url)
        rp.close()
        print('退出成功')
            

    def sign(self): #签到
        # 签到的地址
         url = 'http://www.kuaipan.cn/index.php?ac=common&op=usersign'
         # json.loads 的参数一定是个字符，不能使byte,和py2x 的区别
         # 这里利用json 把返回的数据封装成json格式
         rp = urllib.request.urlopen(url)
         rp_data = rp.read()
         rp_data = rp_data.decode('utf-8', 'ignore')

         sign_data = json.loads(rp_data)
         
         if sign_data['state'] == -102:
             print('今天已经签到了')
             print()
         elif sign_data['state'] ==1:
            print('签到成功')
         else:
            print('签到失败，其他原因')
         
    
    def score(self): # 查看积分
         url = 'http://www.kuaipan.cn/score.htm'
         rp = urllib.request.urlopen(url)
         rp_data = rp.read()
         rp_data = rp_data.decode('utf-8', 'ignore')
         score = rp_data.split('<span class="blue">')[1]
         score = score.split('</span>')[0]
         print('你的积分是 %s' % score)
         
         
    def space(self): #查看网盘容量
         url = 'http://www.kuaipan.cn/index.php?ac=home&op=space'
         rp = urllib.request.urlopen(url)
         rp_data = rp.read()
         rp_data = rp_data.decode('utf-8', 'ignore')
         sign_data = json.loads(rp_data)
         print('你的空间总大小是:  %.2f ' %  float(float(sign_data['xLive']['total'])/1024/1024/1024) +'G')
         print('你的空间已经用了:  %.2f ' %   float(float(sign_data['xLive']['used'])/1024/1024/1024) +'G')
         print('还剩容量: %.2f' % (float(float(sign_data['xLive']['total'])/1024/1024/1024) 
                   - float(float(sign_data['xLive']['used'])/1024/1024/1024)) + 'G')
         
         
         
         



if __name__ == '__main__':
   kk = Login_kp()
   flag = True   
   flag2 = True
   while flag:
     print('请输入')
    # user = input('金山快盘_账号:')
    # pwd = input('金山快盘_密码:')
     
     user ='mail2sujie@gmail.com'
     pwd = 'sujiesujie'
   
     if kk.login(user, pwd) != True:
       continue
     else:
       kk.score()
       while flag2:
          print('请选择命令(签到_sign  查看积分_score  退出账号_out  退出程序_q  查看容量_space)')
          choose = input()
          if choose == 'sign':
             kk.sign() 
          elif choose == 'score':
              kk.score()
          elif choose == 'space':
              kk.space()
          elif choose == 'q':
              exit()
          elif choose == 'logout':
              kk.logout()
              break












