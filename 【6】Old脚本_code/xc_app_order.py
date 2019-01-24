# -*- coding:utf-8 -*-
import pymysql
import cx_Oracle
import sys
# import numpy as np
# import time
# import sched
reload(sys)
sys.setdefaultencoding('utf-8')

mysql_conn = pymysql.connect(
    host='192.168.9.132',
    port=3308,
    user='xcsm',
    passwd='itbt2016',
    db='xcsm',
    charset='utf8',
)

# oracle_conn = cx_Oracle.connect("xccoms001/xccoms001@218.6.173.218:18325/ORCL")
oracle_conn = cx_Oracle.connect("xccoms001/xccoms2018@172.30.10.189:1521/ORCL")

cur_my = mysql_conn.cursor()
cur_or = oracle_conn.cursor()

SQL1 = "SELECT DATE_FORMAT(DATE_SUB(CURDATE(),INTERVAL 1 DAY),'%Y-%m-%d'),companyName,'',shopId,COUNT(orderNo) ,SUM(amount) ,(SUM(amount)/COUNT(orderNo)) FROM xc_order WHERE state = 4 AND shopId LIKE 'Z%' AND paytime<DATE_FORMAT(DATE_SUB(CURDATE(),INTERVAL 1 DAY),'%Y-%m-%d 00:00:00') GROUP BY shopId;"

SQL2 = "SELECT DATE_FORMAT(DATE_SUB(CURDATE(),INTERVAL 1 DAY),'%Y-%m-%d'),companyName,'',shopId,COUNT(orderNo) ,SUM(amount) ,SUM(amount)/COUNT(orderNo) FROM xc_order WHERE state = 4 AND shopId LIKE 'Z%' AND paytime>=DATE_FORMAT(DATE_SUB(CURDATE(),INTERVAL 1 DAY),'%Y-%m-%d 00:00:00') AND paytime<DATE_FORMAT(CURDATE(),'%Y-%m-%d 00:00:00') GROUP BY shopId;"

# SQL3 = "SELECT * FROM XCCOMS.D_STORE_APP_AMOUNT_HIS"

sql1 = "INSERT INTO XCCOMS.D_STORE_APP_AMOUNT_HIS (ETL_DT,BRANCH_COMPANY_NAME,SHOP_NAME,SHOP_CODE, TRANS_CNT, AMOUNT,AVG_AMOUNT) VALUES (TO_DATE(:1,'yyyy-mm-dd'),:2,:3,:4,:5,:6,:7)"

sql2 = "INSERT INTO XCCOMS.D_STORE_APP_AMOUNT_DAILY (ETL_DT,BRANCH_COMPANY_NAME,SHOP_NAME,SHOP_CODE, TRANS_CNT, AMOUNT,AVG_AMOUNT) VALUES (TO_DATE(:1,'yyyy-mm-dd'),:2,:3,:4,:5,:6,:7)"


# 统计小超c端app交易数据：历史交易(不包括当天),并将数据插入XCCOMS.D_STORE_APP_AMOUNT_HIS表中
cur_my.execute(SQL1)
hist_info = cur_my.fetchall()
# print hist_info
# print hist_info[0][1]
for i in range(0, len(hist_info)):
    cur_or.execute(sql1, (hist_info[i][0], hist_info[i][1], hist_info[i][
2], hist_info[i][3], hist_info[i][4], hist_info[i][5], hist_info[i][6]))

# 统计小超c端app交易数据：当天交易(当天统计前一天),并将数据插入XCCOMS.D_STORE_APP_AMOUNT_HIS表中
cur_my.execute(SQL2)
day_info = cur_my.fetchall()
for i in range(0, len(day_info)):
    cur_or.execute(sql2, (day_info[i][0], day_info[i][1], day_info[i][2], day_info[
                   i][3], day_info[i][4], day_info[i][5], day_info[i][6]))


# cur_or.execute(SQL3)
# info = cur_or.fetchall()

cur_my.close()
cur_or.close()
oracle_conn.commit()
oracle_conn.close()
mysql_conn.commit()
mysql_conn.close()
print('end')


# def time_run(sched_time):
#     flag = 0
#     while True:
#         now = datetime.datetime.now()
#         if now == sched_time:
#             run_task()
#             flag = 1
#         else:
#             if flag == 1:
#                 sched_time = sched_time + datetime.timedelta(hours=1)
#                 flag = 0
# sched_time = datetime.datetime(2018, 1, 9, 16, 00, 00, 00)
# print time_run(sched_time)
