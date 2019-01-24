# -*- coding:utf-8 -*-
import pymysql
import pandas as pd
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

conn = pymysql.connect(host='192.168.0.84', port=9999,
                       user='caosn', passwd='mXOqIJmG', db='itbtdb', charset='utf8')

cur = conn.cursor()

credit_data = pd.read_sql(
    "SELECT a.user_id, u.username, IFNULL(b.sum1, 0) AS t_sum, a.sum1 AS q_sum, IFNULL(c.sum1, 0) AS change_sum, IFNULL(d.cons, 0) AS change_cons FROM ( SELECT user_id, SUM(`value`) sum1 FROM itd_credit_log_3 WHERE type_id = 317 AND addtime >= UNIX_TIMESTAMP('20170321') GROUP BY user_id ) a LEFT JOIN ( SELECT user_id, SUM(`value`) sum1 FROM itd_credit_log_3 WHERE type_id = 7 AND addtime >= UNIX_TIMESTAMP('20170321') GROUP BY user_id ) b ON a.user_id = b.user_id LEFT JOIN ( SELECT user_id, SUM(`value`) sum1 FROM itd_credit_log_3 WHERE type_id = 31 AND addtime >= UNIX_TIMESTAMP('20170321') GROUP BY user_id ) c ON a.user_id = c.user_id LEFT JOIN ( SELECT user_id, COUNT(user_id) cons FROM itd_credit_log_3 WHERE type_id = 31 AND addtime >= UNIX_TIMESTAMP('20170321') GROUP BY user_id ) d ON a.user_id = d.user_id LEFT JOIN itd_iuser u ON a.user_id = u.user_id;", con=conn)  # 签到积分、投资积分、积分兑换、积分兑换次数

credit_day = pd.read_sql("SELECT * FROM ( SELECT * FROM ( SELECT user_id, MAX(days) AS lianxu_days, MIN(login_day) AS start_date, MAX(login_day) AS end_date FROM ( SELECT user_id, @count_day := ( CASE WHEN ( @last_userid = user_id AND DATEDIFF(add_time ,@last_dt) = 1 ) THEN (@count_day + 1) WHEN ( @last_userid = user_id AND DATEDIFF(add_time ,@last_dt) < 1 ) THEN (@count_day + 0) ELSE 1 END ) AS days, ( @count_ix := ( @count_ix + IF (@count_day = 1, 1, 0))) AS count_ix, @last_userid := user_id, @last_dt := add_time AS login_day FROM ( SELECT user_id, FROM_UNIXTIME(addtime) AS add_time FROM itd_credit_log_3 WHERE type_id = 317 AND addtime >= UNIX_TIMESTAMP('20170321') ORDER BY user_id, addtime) AS t, ( SELECT @last_userid := '' ,@last_dt := '' ,@count_ix := 0 ,@count_day := 0 ) AS t1 ) AS t2 GROUP BY user_id, count_ix HAVING lianxu_days > 0 ) AS tmp ORDER BY lianxu_days DESC ) ntmp GROUP BY user_id ORDER BY user_id ASC;", con=conn)  # 最大连续签到天数统计

print credit_day.loc[:, ['lianxu_days']]
credit_data.insert(6, 'lianxu_days', credit_day.loc[:, ['lianxu_days']])
print credit_data
credit_data.to_csv('credit_data.csv',index=False)


cur.close()
conn.commit()
conn.close()
print('end')
