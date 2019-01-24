# -*- coding:utf-8 -*-
import pymysql
import numpy as np
import pandas as pd
import chardet
"""
chardet模块中的chardet.detect()函数查看当前 字符串编码格式
"""
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='csn_db',
    charset='utf8'
)

cur = conn.cursor()

SQL = "INSERT INTO db_hostip_91_112(userid,hostip,counts) VALUES(%s,%s,%s);"


def loadDateSet(filename, encoding='utf-8'):
    dataSet = []
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split('\t')  # 以空白符为分割，并删除首、尾处的空白符
        # fltLine = map(string, curLine)  # map函数将curLine中的所有元素都转化成float
        dataSet.append(curLine)  # 向空列表dataMat中追加元素
    return dataSet


filename = "hostip9.1-11.2"  # 数据文件
dataSet = loadDateSet(filename)  # 载入数据集
print dataSet[0]
print len(dataSet)
print chardet.detect(dataSet[0][1])
print dataSet[0][1].decode('utf-8')

for i in range(0, len(dataSet)):
    # dataSet[i][1] = dataSet[i][1].decode('utf-8')
    # print dataSet[i][1]
    cur.execute(SQL, (dataSet[i][0], dataSet[i][1].decode('utf-8'), dataSet[i][2]))

cur.close()
conn.commit()
conn.close()
print('end')



# 134144
# 138040
# data_host = pd.read_table("hostip2", sep=',')
# print data_host
# print data_host.shape
# print data_host.head
# print data_host.dtypes
# # data_host.rename(columns = {'userid', 'hostip', '次数'},inplace=ture)
# print data_host.columns
# print data_host.groupby('userid')
