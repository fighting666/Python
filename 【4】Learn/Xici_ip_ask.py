#!./usr/bin/env.python
# -*- coding:utf-8 -*-
import urllib2
import os
import re
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='csn_db'
)
cur = conn.cursor()


def dowload_ip(url):
    for page_num in range(1, 50):
        ask_url = url + str(page_num)

        headers = {
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
        req = urllib2.Request(ask_url, headers=headers)
        response = urllib2.urlopen(req)
        html = response.read()

        ip = re.findall(
            r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])', html)
        # port=re.findall(r'([1-9]\d\d\d\d|)')
        # position = re.findall(r'<a href=".*?">(.*?)</a>', html)
        # types = re.findall(r'<td class="country">(.*?)</td>', html)
        # print '---------------------------第%d页------------------------------'
        # % (page_num)
        iplist = []
        for ips in ip:
            iplist.append(str(ips))
            print iplist

            # sation=[]
            # for i in position:
            #     sation.append(str(i))
            #
            # stata=[]
            # for i in types:
            #     stata.append(str(i))

            # for n in range(len(iplist)):
            #     print 'IP:%s' % (iplist[n])
            # print 'IP:%s 位置:%s 类型:%s' % (iplist[n],sation[n],stata[n])
            # for n in range(len(iplist)):
            #     sql1 = ("INSERT INTO db_iplist(ip)" "VALUES(%s)")
            #     cur.execute(sql1,n)

url = 'http://www.xicidaili.com/nn/'
print dowload_ip(url)

cur.close()
conn.commit()
conn.close()
print('end')
