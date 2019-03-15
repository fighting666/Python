# -*- coding:utf-8 -*-
import pymysql
import numpy as np
import pandas as pd
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

plat = ['2ccccd865351621ae3ce8d78ced0bff7',
        '94cd0e6a95dbee683a915f3c0f9ff068',
        'f545569cbdc3155e6c0ee2d92a571e8e',
        'a47d3d02162826c54d29d77423da8a23',
        '655c4820bb69e9b1b997a2cac30d40df',
        '65724569467cba1e7bdb07ec99ca597f',
        '210117f4066125b0f89b29ea0926e5e5',
        '6ddb32b7fe9b35263abfd55b796a647f',
        'f955f1cf1d1127ccf426d50092ce8e68',
        '41876a2da7e7f32b8bd2d7ded64d5f8a',
        '58d8daa11ec052cf1dcf5aee46f5a14e']

# 新注册用户
SQL1 = "SELECT p.iuser_uid, u.username, u.phone, CASE u.real_status WHEN 1 THEN '已实名' WHEN 0 THEN '未实名' END, FROM_UNIXTIME(p.addtime), u.addip, CASE u.from_where WHEN 1 THEN 'PC' WHEN 2 THEN '移动端' WHEN 3 THEN '微信' END, a.`name` FROM itd_plat AS p LEFT JOIN itd_iuser AS u ON p.iuser_uid = u.user_id LEFT JOIN itd_award_activities_info AS a ON p.plat = a.activities_code WHERE p.iuser_uid IN ( SELECT iuser_uid FROM itd_plat WHERE plat = %s AND addtime >= UNIX_TIMESTAMP('2017-10-01 00:00:00') AND addtime < UNIX_TIMESTAMP('2019-01-01 23:59:59')) AND p.addtime >= UNIX_TIMESTAMP('2018-01-18 00:00:00') AND p.addtime < UNIX_TIMESTAMP('2018-01-22 00:00:00') ORDER BY FROM_UNIXTIME(p.addtime) ASC;"

# 实名用户
SQL2 = "SELECT v.user_id, u.username, u.phone, FROM_UNIXTIME(v.verifydate1), v.verifyexp1, a.`name` FROM itd_verify AS v LEFT JOIN itd_iuser AS u ON v.user_id = u.user_id LEFT JOIN itd_plat AS p ON v.user_id = p.iuser_uid LEFT JOIN itd_award_activities_info AS a ON p.plat = a.activities_code WHERE v.user_id IN ( SELECT iuser_uid FROM itd_plat WHERE plat = %s AND addtime >= UNIX_TIMESTAMP('2017-10-01 00:00:00') AND addtime < UNIX_TIMESTAMP('2019-01-01 23:59:59')) AND v.verifydate1 >= UNIX_TIMESTAMP('2018-01-18 00:00:00') AND v.verifydate1 < UNIX_TIMESTAMP('2018-01-22 00:00:00') AND v.etype = '102' AND u.real_status = 1 ORDER BY FROM_UNIXTIME(v.verifydate1) ASC;"

# 充值
SQL3 = "SELECT r.user_id, u.username, u.phone, r.money, FROM_UNIXTIME(r.verify_time), p.`name`, CASE r.rechargeway WHEN 0 THEN 'PC' WHEN 1 THEN '微信' WHEN 2 THEN '移动端' END, a.`name` FROM itd_iaccount_recharge AS r LEFT JOIN itd_iuser AS u ON r.user_id = u.user_id LEFT JOIN itd_payment AS p ON r.payment = p.id LEFT JOIN itd_plat AS q ON r.user_id = q.iuser_uid LEFT JOIN itd_award_activities_info AS a ON q.plat = a.activities_code WHERE r.user_id IN ( SELECT iuser_uid FROM itd_plat WHERE plat = %s AND addtime >= UNIX_TIMESTAMP('2017-10-01 00:00:00') AND addtime < UNIX_TIMESTAMP('2019-01-01 23:59:59')) AND r.verify_time >= UNIX_TIMESTAMP('2018-01-18 00:00:00') AND r.verify_time < UNIX_TIMESTAMP('2018-01-22 00:00:00') AND r.`status` = 1 ORDER BY FROM_UNIXTIME(r.verify_time) ASC;"

# 用户提现信息统计
SQL4 = "SELECT c.user_id, u.username, u.phone, c.credited, FROM_UNIXTIME(c.verify_time), a.`name` FROM itd_iaccount_cash AS c LEFT JOIN itd_iuser AS u ON c.user_id = u.user_id LEFT JOIN itd_plat AS p ON c.user_id = p.iuser_uid LEFT JOIN itd_award_activities_info AS a ON p.plat = a.activities_code WHERE c.user_id IN ( SELECT iuser_uid FROM itd_plat WHERE plat IN ('2ccccd865351621ae3ce8d78ced0bff7','94cd0e6a95dbee683a915f3c0f9ff068','f545569cbdc3155e6c0ee2d92a571e8e','a47d3d02162826c54d29d77423da8a23','655c4820bb69e9b1b997a2cac30d40df','65724569467cba1e7bdb07ec99ca597f','210117f4066125b0f89b29ea0926e5e5','6ddb32b7fe9b35263abfd55b796a647f','f955f1cf1d1127ccf426d50092ce8e68','41876a2da7e7f32b8bd2d7ded64d5f8a','58d8daa11ec052cf1dcf5aee46f5a14e') AND addtime >= UNIX_TIMESTAMP('2017-10-01 00:00:00') AND addtime < UNIX_TIMESTAMP('2019-01-01 23:59:59')) AND c.`status` = 1 AND c.verify_time >= UNIX_TIMESTAMP('2018-01-18 00:00:00') AND c.verify_time < UNIX_TIMESTAMP('2018-01-22 00:00:00') ORDER BY FROM_UNIXTIME(c.verify_time) ASC;"

# 用户红包使用金额统计
SQL5 = "SELECT c.user_id, u.username, u.phone, c.`value`, a.`name` FROM itd_treasure_chest AS c LEFT JOIN itd_iuser AS u ON c.user_id = u.user_id LEFT JOIN itd_iborrow_tender AS t ON c.tnum = t.tender_num LEFT JOIN itd_iborrow AS b ON t.borrow_num = b.borrow_num LEFT JOIN itd_plat AS p ON c.user_id = p.iuser_uid LEFT JOIN itd_award_activities_info AS a ON p.plat = a.activities_code WHERE c.user_id IN ( SELECT iuser_uid FROM itd_plat WHERE plat IN ('2ccccd865351621ae3ce8d78ced0bff7','94cd0e6a95dbee683a915f3c0f9ff068','f545569cbdc3155e6c0ee2d92a571e8e','a47d3d02162826c54d29d77423da8a23','655c4820bb69e9b1b997a2cac30d40df','65724569467cba1e7bdb07ec99ca597f','210117f4066125b0f89b29ea0926e5e5','6ddb32b7fe9b35263abfd55b796a647f','f955f1cf1d1127ccf426d50092ce8e68','41876a2da7e7f32b8bd2d7ded64d5f8a','58d8daa11ec052cf1dcf5aee46f5a14e' ) AND addtime >= UNIX_TIMESTAMP('2017-10-01 00:00:00') AND addtime < UNIX_TIMESTAMP('2019-01-01 23:59:59')) AND c.ruleType = '1001' AND c.`status` = 2 AND t.`status` = 1 AND b.repayment_time >= UNIX_TIMESTAMP('2018-01-18 00:00:00') AND b.repayment_time < UNIX_TIMESTAMP('2018-01-22 00:00:00') ORDER BY FROM_UNIXTIME(b.repayment_time);"

# 新建一张excel表，存储统计结果
table_add_user = pd.ExcelWriter('add_user.xlsx')
table_real_user = pd.ExcelWriter('real_user.xlsx')
table_recharge = pd.ExcelWriter('recharge.xlsx')

# 将新注册、实名、充值用户信息统计写入excel中
for i in range(len(plat)):
    cur.execute(SQL1, str(plat[i]))
    add_user = cur.fetchall()
    add_user1 = pd.DataFrame(np.array(add_user))
    # print add_user1
    str1 = plat[i]
    add_user1.to_excel(
        table_add_user, str1[-4:], index=False, encoding='utf_8')

    cur.execute(SQL2, str(plat[i]))
    real_user = cur.fetchall()
    real_user1 = pd.DataFrame(np.array(real_user))
    # print real_user1
    str2 = plat[i]
    real_user1.to_excel(
        table_real_user, str2[-4:], index=False, encoding='utf_8')

    cur.execute(SQL3, str(plat[i]))
    recharge = cur.fetchall()
    recharge1 = pd.DataFrame(np.array(recharge))
    # print can_cash1
    str3 = plat[i]
    recharge1.to_excel(
        table_recharge, str3[-4:], index=False, encoding='utf_8')

    print str1[-4:], int(add_user1.iloc[:, 0].count()), int(real_user1.iloc[:, 0].count()), int(recharge1.iloc[:, 0].count())


table_ti_red = pd.ExcelWriter('tixian_red.xlsx')

tixian = pd.read_sql(SQL4, con=conn)
tixian.to_excel(table_ti_red, 'tixian', index=False)
print int(tixian.iloc[:, 0].count()), int(tixian.iloc[:, 3].sum())

red_cash = pd.read_sql(SQL5, con=conn)
red_cash.to_excel(table_ti_red, 'red_cash', index=False)
print int(red_cash.iloc[:, 0].count()), int(red_cash.iloc[:, 3].sum())

table_add_user.save()
table_real_user.save()
table_recharge.save()
table_ti_red.save()
table_add_user.close()
table_real_user.close()
table_recharge.close()
table_ti_red.close()

cur.close()
conn.commit()
conn.close()
print('end')

# bff7 0 0 19
# f068 0 0 5
# 1e8e 11 11 425
# 8a23 8 7 13
# 40df 1 1 1
# 597f 1 0 0
# e5e5 0 0 22
# 647f 0 0 0
# 8e68 6 7 1334
# 5f8a 2 2 0
# a14e 2 2 2
# 337 35607909
# 3482 480070
