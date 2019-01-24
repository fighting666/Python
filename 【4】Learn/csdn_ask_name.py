# -*- coding:utf-8 -*-
import pymysql
import numpy as np
import pandas as pd
import re
import urllib2
import random

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='csn_db',
    charset='utf8'
)

cur = conn.cursor()


def save_username(url):
    for page_num in range(1, 30):
        ask_url = url + 'p' + str(page_num)

        agent_list = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 1.0; en-us; dream) AppleWebKit/525.10 (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2',
                      'Mozilla/5.0 (Linux; U; Android 1.1; en-gb; dream) AppleWebKit/525.10 (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2', 'Mozilla/5.0 (Linux; U; Android 1.5; de-de; Galaxy Build/CUPCAKE) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 ', ]
        user_agent = random.choice(agent_list)
        headers = {'User-Agent': user_agent}

        req = urllib2.Request(ask_url, headers=headers)
        response = urllib2.urlopen(req)
        html = response.read().decode('utf-8')

        p = r'<a class="user_name" href=".*?" target="_blank">(.*?)</a>'
        username = re.findall(p, html)

        namelist = []
        for names in username:
            namelist.append(str(names))
        print namelist

        # for i in range(len(namelist)):
        #     print namelist[i]
        # for i in range(1, len(namelist)):
        #     sql = 'INSERT INTO db_username1(username) VALUES(%s)'
        #     cur.execute(sql, namelist[i].decode('utf-8'))


url = 'http://ask.csdn.net/'
print save_username(url)

cur.close()
conn.commit()
conn.close()
print('end')

#----------------------------------------------------------------------------------------------------------------#

# #csdn博客文章点击量爬取（示例）
# # 当前的博客列表页号
# page_num = 1
# # 不是最后列表的一页
# notLast = 1

# account = str(raw_input('输入csdn的登录账号:'))

# while notLast:

#     # 首页地址
#     baseUrl = 'http://blog.csdn.net/' + account
#     # 连接页号，组成爬取的页面网址
#     myUrl = baseUrl + 'p' + str(page_num)

#     # 伪装成浏览器访问，直接访问的话csdn会拒绝
#     user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0'
#     headers = {'User-Agent': user_agent}
#     # 构造请求
#     req = urllib2.Request(myUrl, headers=headers)

#     # 访问页面
#     myResponse = urllib2.urlopen(req)
#     myPage = myResponse.read()

#     # 在页面中查找是否存在‘尾页’这一个标签来判断是否为最后一页
#     notLast = re.findall('<a href=".*?">尾页</a>', myPage, re.S)

#     print ('-----------------------------第%d页---------------------------------' % (page_num,))

#     # 利用正则表达式来获取博客的标题
#     title = re.findall(
#             '<span class="link_title"><a href=".*?">(.*?)</a></span>', myPage, re.S)

#     titleList = []
#     for items in title:
#         titleList.append(str(items).lstrip().rstrip())

#     # 利用正则表达式获取博客的评论处的用户名
#     view = re.findall(
#             '<span class="link_view".*?><a href=".*?" title="阅读次数">阅读</a>\((.*?)\)</span>', myPage, re.S)

#     viewList = []
#     for items in view:
#         viewList.append(str(items).lstrip().rstrip())

#     # 将结果输出
#     for n in range(len(titleList)):
#         print ('访问量:%s 标题:%s' % (viewList[n].zfill(4), titleList[n]))

#     # 页号加1
#     page_num = page_num + 1

#----------------------------------------------------------------------------------------------------------------#

# #简书网站用户名爬取
# def get_name(url):
#     for page in range(1, 30):
#         get_url = url + str(page)

#         agent_list = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 1.0; en-us; dream) AppleWebKit/525.10 (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2',
#                       'Mozilla/5.0 (Linux; U; Android 1.1; en-gb; dream) AppleWebKit/525.10 (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2', 'Mozilla/5.0 (Linux; U; Android 1.5; de-de; Galaxy Build/CUPCAKE) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 ', ]
#         user_agent = random.choice(agent_list)
#         headers = {'User-Agent': user_agent}

#         req = urllib2.Request(get_url, headers=headers)
#         response = urllib2.urlopen(req)
#         html = response.read()

#         names = r'<a class="blue-link" target="_blank" href=".*?">(.*?)</a>'
#         username = re.findall(names, html)

#         namelist = []
#         for uname in username:
#             namelist.append(uname)

#         for i in range(1, len(namelist)):
#             print namelist[i].decode('utf-8')

#         # for i in range(1, len(namelist)):
#         #     sql = 'INSERT INTO db_username(username) VALUES(%s);'
#         #     cur.execute(sql, (namelist[i].decode('utf-8')))

# url = 'http://www.jianshu.com/c/Jgq3Wc?order_by=added_at&page='
# print get_name(url)

# cur.close()
# conn.commit()
# conn.close()
# print('end')
#----------------------------------------------------------------------------------------------------------------#
