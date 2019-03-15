#-*- coding:utf-8 -*-
import requests
import threading
import time

# 需要执行的函数


def login(asseturl):
    cookieurl = 'https://trunk.yatang.cn/NewLogin/setcode/sign/loginnobody'
    loginurl = 'https://trunk.yatang.cn/index.php?s=/new_login/checklogin'
    a = requests.get(cookieurl)
    datapost = {
        'username': 'wang0502',
        'password': 'XcXorif99EPlbXd0',
        'cookietime': '30',
        'referer': 'https://trunk.yatang.cn/index.php?s=/index/index Name'
    }
    response = requests.post(loginurl, datapost, cookies=a.cookies)
    print response
    biao_list = requests.get(asseturl)
    print(biao_list.text)

# 每隔5秒钟执行一次login函数，请求一次标页面


def login2():
    asseturl = 'https://trunk.yatang.cn/Financial/asset'
    while 1:
        login(asseturl)
        time.sleep(1)

if __name__ == '__main__':
    biao = threading.Thread(target=login2)
    biao.start()
    biao.join()

#-----------------------------------------------------------------------------------------------------------#
# 第一次用脚本登录网页
# # 验证码地址和post地址
# captchaurl = "https://trunk.yatang.cn/index.php?s=/NewLogin/verify/"
# posturl = "https://trunk.yatang.cn/NewLogin/index/referer/"
# # 将cookies绑定到一个opener cookie由cookielib自动管理
# cookie = cookielib.CookieJar()
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# # 用openr访问验证码地址,获取cookie
# # picture = opener.open(captchaurl).read()
# # # # 保存验证码到本地
# # local = open('D:/python/learn/image.jpg', 'wb')
# # local.write(picture)
# # local.close()
# # # 打开保存的验证码图片 输入
# # secretcode = raw_input('输入验证码：')
# postdata = {
#     'username': 'parker',
#     'password': 'XcXorif99EPlbXd0',
#     'cookietime': '30',
#     'referer': 'https://trunk.yatang.cn/index.php?s=/index/index'}
# headers = {
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.8',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# # 根据抓包信息 构造headers
# request = urllib2.Request(
#     posturl, data=urllib.urlencode(pastdata), headers=headers)
# url = opener.open(request)
# print url.info()

# try:
#     response = opener.open(request)
#     result = response.read().decode('gb2312')
#     print result
# except urllib2.HTTPError as e:
#     print e.code


# import requests
# a = requests.get('https://trunk.yatang.cn/NewLogin/setcode/sign/loginnobody')
# r = requests.post('https://trunk.yatang.cn/index.php?s=/new_login/checklogin', data={
#                   'username': 'xaopp', 'password': '6r4KWCcxlPj5shTQ', 'cookietime': '30', 'referer': 'https://trunk.yatang.cn/index.php?s=/index/index Name'}, cookies=a.cookies)
# aa = requests.get('https://trunk.yatang.cn/Financial/asset')
# print(aa.text)
