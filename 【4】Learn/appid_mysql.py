# -*- coding:utf-8 -*-
import pymysql
import numpy as np
import pandas as pd

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='csn_db',
    charset='utf8')

cur = conn.cursor()

SQL = "INSERT INTO db_appid_0926(userid,appid,counts) VALUES(%s,%s,%s);"


def loadDateSet(filename):
    dataSet = []
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split('\t')  # 以空白符为分割，并删除首、尾处的空白符
        # fltLine = map(string, curLine)  # map函数将curLine中的所有元素都转化成float
        dataSet.append(curLine)  # 向空列表dataMat中追加元素
    return dataSet

filename = "D:\\python\\learn\\data\\appid0926"  # 数据文件
dataSet = loadDateSet(filename)  # 载入数据集
# print np.array(dataSet)
# print dataSet
print dataSet[0]
print len(dataSet)
print dataSet[(len(dataSet) - 1)]
print dataSet[0][0]
print dataSet[0][1]

for i in range(0, len(dataSet)):
    cur.execute(SQL, (dataSet[i][0], dataSet[i][1], dataSet[i][2]))

cur.close()
conn.commit()
conn.close()
print('end')

# 47785
# 49100
