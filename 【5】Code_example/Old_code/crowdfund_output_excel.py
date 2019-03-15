# -*- coding:utf-8 -*-
import pymysql
import pandas as pd
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

conn = pymysql.connect(host='192.168.0.84',
                       port=9999,
                       user='caosn',
                       passwd='mXOqIJmG',
                       db='itbtdb',
                       charset='utf8')

cur = conn.cursor()

# sql0读取众筹项目号及满标时间
SQL0 = "SELECT id, DATE_FORMAT( crowdfunding_full_time, '%Y-%m-%d 00:00:00' ) '满标时间', financing_amount '众筹金额' FROM itd_crowdfunding_item WHERE crowdfunding_full_time >= '2018-01-18 00:00:00' GROUP BY id;"

# SQL1读取每个项目的投资人信息
SQL1 = "SELECT t.user_name '用户名', u.phone '手机号', SUM(t.investment_amount_actual) '实际投资金额', SUM(t.invest_amount_own) '自有投资金额', SUM(t.invest_amount_financing) '融资投资金额', IFNULL( IF ( a.`name` IS NULL, m.site_name, a.`name` ), '无' ) '注册渠道', FROM_UNIXTIME(u.addtime) '注册时间' FROM itd_crowdfunding_invest_detail AS t LEFT JOIN itd_iuser AS u ON t.user_id = u.user_id LEFT JOIN ( SELECT iuser_uid, plat FROM itd_plat GROUP BY iuser_uid ) AS p ON t.user_id = p.iuser_uid LEFT JOIN itd_award_activities_info AS a ON p.plat = a.activities_code LEFT JOIN itd_promotion AS m ON p.plat = m.site_code WHERE t.crowdfunding_item_id=%s GROUP BY t.user_id ORDER BY t.user_id;"

# SQL2投资人是否为纯投资用户
SQL2 = "SELECT a.user_id '用户ID', IF ( b.borrow_num IS NULL, '是', '否' ) '是否为纯投资用户' FROM ( SELECT DISTINCT user_id FROM itd_crowdfunding_invest_detail WHERE crowdfunding_item_id = %s GROUP BY user_id ) AS a LEFT JOIN itd_iborrow AS b ON a.user_id = b.user_id AND b.`status` IN (7, 8) AND FROM_UNIXTIME(b.addtime) < %s GROUP BY a.user_id ORDER BY a.user_id;"

# SQL3投资人历史投资次数及金额
SQL3 = "SELECT a.user_id '用户ID', COUNT(b.user_id) '历史参与众筹的次数', SUM( ifnull( b.investment_amount_actual, 0 )) '历史投资金额' FROM ( SELECT DISTINCT user_id FROM itd_crowdfunding_invest_detail WHERE crowdfunding_item_id = %s GROUP BY user_id ) AS a LEFT JOIN itd_crowdfunding_invest_detail AS b ON a.user_id = b.user_id AND b.crowdfunding_item_id NOT IN ( '1', '2', '8', '33', '34', '35', '36', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '60', '61', '62', '65', '68', '74', '76', '77', '79', '84', '87', '118', '147', '167', '168', '169', '170', '172', '176','426','462','463','464','465','486' ) AND b.tender_time < %s GROUP BY a.user_id ORDER BY a.user_id;"

# 读取众筹项目号及满标时间
cur.execute(SQL0)
item_data = cur.fetchall()
# print pd.DataFrame(np.array(item_data))

# 新建一张excel表，存储统计结果
table = pd.ExcelWriter('01.18-01.21crowding.xlsx')


for item_data1 in item_data:
    cur.execute(SQL1, int(item_data1[0]))
    info_data = cur.fetchall()
    #print info_data
    list1 = pd.Series(
        ['用户名', '手机号', '实际投资金额', '自有投资金额', '融资投资金额', '注册渠道', '注册时间'])
    info_data1 = pd.DataFrame(np.array(info_data), columns=list1)
    #print info_data1

    cur.execute(SQL2, ((int(item_data1[0])), item_data1[1]))
    borw_times = cur.fetchall()
    list2 = pd.Series(['用户ID', '是否为纯投资用户'])
    borw_times1 = pd.DataFrame(np.array(borw_times), columns=list2)
    # print borw_times1

    cur.execute(SQL3, ((int(item_data1[0])), item_data1[1]))
    tender_times = cur.fetchall()
    list3 = pd.Series(['用户ID', '历史参与众筹的次数', '历史投资金额'])
    tender_times1 = pd.DataFrame(np.array(tender_times), columns=list3)
    # print tender_times1

    # 将SQL2、SQL3统计结果的指定行插入SQL1数据框中
    info_data1.insert(7, '是否为纯投资用户', borw_times1.loc[:, ['是否为纯投资用户']])
    info_data1.insert(8, '历史参与众筹的次数', tender_times1.loc[:, ['历史参与众筹的次数']])
    info_data1.insert(9, '历史投资金额', tender_times1.loc[:, ['历史投资金额']])
    # print info_data1
    # print 'table_%s' % (item_data1[0])

    # 将合并后的数据框写入excel表中的不同sheet表中
    info_data1.to_excel(table, 'table_%s' %
                        (item_data1[0]), index=False, encoding='utf_8')

    print 'table_%s' % (item_data1[0]), int(info_data1.loc[:, ['用户名']].count()), int(info_data1.loc[:, ['实际投资金额']].sum()), item_data1[1], int(info_data1.loc[:, ['历史参与众筹的次数']].sum()), int(info_data1.loc[:, ['历史投资金额']].sum())


# ExcelWriter.save()
# ExcelWriter.close()
table.save()
table.close()
cur.close()
conn.commit()
conn.close()
print('end')

# item_data = pd.read_sql(SQL0, con=conn)
# info_data = pd.read_sql(SQL1, con=conn)
# borw_times = pd.read_sql(SQL2, con=conn)
# tender_times = pd.read_sql(SQL3, con=conn)

# table_494 111 10000000 2018-01-18 00:00:00 15827 347206500
# table_501 158 8000000 2018-01-20 00:00:00 18061 413204400
# table_507 46 600000 2018-01-19 00:00:00 2446 24374000
# table_508 102 2000000 2018-01-19 00:00:00 13918 254707900
# table_509 22 1000000 2018-01-20 00:00:00 5375 96049600