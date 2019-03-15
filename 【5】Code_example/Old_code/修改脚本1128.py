# -*- coding:utf-8 -*-
import pymysql
import numpy as np

conn = pymysql.connect(
    host='192.168.0.84',
    port=9999,
    user='caosn',
    passwd='mXOqIJmG',
    db='itbtdb',
)
# conn = pymysql.connect(
#     host='114.55.28.159',
#     port=6606,
#     user='root',
#     passwd='itbt2016',
#     db='itbtdb',
# )
cur = conn.cursor()

execSQL0 = "SELECT iuser_uid,SUBSTR(iuser_uid,-1) FROM itd_plat WHERE plat IN('1eecc4f732945306513c10cd029ab35f') AND FROM_UNIXTIME(addtime)>='2017-11-01 00:00:00';"
# execSQL0 = "SELECT user_id,SUBSTR(user_id,-1) FROM itd_iuser WHERE user_id='561021';"
execSQL1 = "SELECT id,user_id,num,type,use_change,nouse_change,addtime,btype,principal FROM itd_iaccount_log_%s WHERE user_id=%s AND FROM_UNIXTIME(addtime)>='2017-11-01 00:00:00' ORDER BY id ASC;"
execSQL2 = "SELECT b.borrow_type,b.`status`,b.time_limit,b.repaystyle,b.repayment_time,b.borrow_num FROM itd_iborrow_tender AS a LEFT JOIN itd_iborrow AS b ON a.borrow_num=b.borrow_num WHERE a.borrow_num=%s or a.tender_num=%s;"
SQL1 = 'INSERT INTO itd_iaccount_log_t1(num,user_id,type,chargemoney,ctendermoney,use_money,btype,time_limit,repaystyle,status,addtime,repayment_time) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
SQL2 = 'SELECT borrow_num FROM itd_iborrow_tender WHERE tender_num=%s LIMIT 1;'
SQL3 = 'SELECT b.borrow_type,b.borrow_num FROM itd_iborrow_repayment AS a LEFT JOIN itd_iborrow AS b ON a.borrow_num=b.borrow_num WHERE a.repayment_num=%s LIMIT 1;'
SQL4 = 'SELECT IFNULL(user_constraint,0),IFNULL(`value`,0) FROM itd_treasure_chest WHERE tnum=%s;'
SQL5 = "SELECT business_code FROM itd_crowdfunding_invest_detail WHERE id=%s limit 1;"

cur.execute(execSQL0)
userid = cur.fetchall()
# print np.array(userid)

for userid1 in userid:
    charge = 0  # 新充值资金
    tender = 0  # 新充值资金投资金额
    miao = []  # 记录新充值投秒资金
    bnum = []  # 记录新充值投秒的标编码
    ninemiao = 0
    tre = []  # 红包资金
    cash = []  # 记录用于抢现金劵的新充值资金
    cnum = []  # 记录新充值抢现金券的id
    cur.execute(execSQL1, (int(userid1[1]), userid1[0]))
    info1 = cur.fetchall()
    # print np.array(info1)
    for info in info1:
        cur.execute(execSQL2, (info[2], info[2]))
        borrow = cur.fetchone()
        if (borrow == None):
            borrow = [0, 0, 0, 0, 0, 0]
        # print borrow
        # 线上、线下充值、电商退货、奖励退款业务
        if (info[3] == 301 or info[3] == 302 or info[3] == 669 or info[3] == 8888):
            if (charge <= 0):
                charge = 0
                tender = 0
                charge += info[4]
                cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                            4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
            else:
                charge += info[4]
                cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                            4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))

        # 104投资、507股权投资、202自动投资、20052抢现金券业务
        elif (info[3] == 104 or info[3] == 557 or info[3] == 202 or info[3] == 20052):
            if (info[6] >= 1504167600):
                if (charge <= 0):
                    charge = 0
                    tender = 0
                elif (charge > 0):
                    cur.execute(SQL2, info[2])
                    bN = cur.fetchall()
                    if (charge >= abs(info[4])):
                        if (info[3] == 104):
                            charge -= abs(info[4])
                            tender = abs(info[4])
                            cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                        4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
                            miao.append(tender)
                            for bN1 in bN:
                                bnum.append(bN1[0])
                        elif (info[3] == 557):
                            cur.execute(SQL5, info[2])
                            business_code = cur.fetchall()
                            charge -= abs(info[4])
                            tender = abs(info[4])
                            cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                        4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
                        elif (info[3] == 202):
                            charge -= abs(info[4])
                            tender = abs(info[4])
                            cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                        4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
                        elif (info[3] == 20052):
                            charge -= abs(info[4])
                            tender = abs(info[4])
                            cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                        4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
                            cash.append(tender)
                            cnum.append(info[2])
                    else:
                        if (info[3] == 104):
                            tender = charge
                            for bN1 in bN:
                                bnum.append(bN1[0])
                            miao.append(tender)
                            charge = 0
                            cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                        4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
                        elif (info[3] == 557):
                            cur.execute(SQL5, info[2])
                            business_code = cur.fetchall()
                            tender = charge
                            charge = 0
                            cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                        4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
                        elif (info[3] == 202):
                            tender = charge
                            charge = 0
                            cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                        4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
                        elif (info[3] == 20052):
                            tender = charge
                            cnum.append(info[2])
                            cash.append(tender)
                            charge = 0
                            cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                        4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
            else:
                if (charge <= 0):
                    charge = 0
                    tender = 0
                elif (charge > 0):
                    cur.execute(SQL2, info[2])
                    bN = cur.fetchall()
                    if (charge >= abs(info[4])):
                        if (info[3] == 104):
                            cur.execute(SQL4, info[2])
                            tre = cur.fetchall()
                            if (len(tre) == 0):
                                tre = [(0, 0)]
                            charge -= abs(info[4]) - tre[0][1]
                            tender = abs(info[4]) - tre[0][1]
                            cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                        4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
                            miao.append(tender)
                            for bN1 in bN:
                                bnum.append(bN1[0])
                        elif (info[3] == 557):
                            cur.execute(SQL5, info[2])
                            business_code = cur.fetchall()
                            cur.execute(SQL4, business_code)
                            tre = cur.fetchall()
                            if (len(tre) == 0):
                                tre = [(0, 0)]
                            charge -= abs(info[4]) - tre[0][1]
                            tender = abs(info[4]) - tre[0][1]
                            cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                        4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
                        elif (info[3] == 202):
                            cur.execute(SQL4, info[2])
                            tre = cur.fetchall()
                            if (len(tre) == 0):
                                tre = [(0, 0)]
                            charge -= abs(info[4]) - tre[0][1]
                            tender = abs(info[4]) - tre[0][1]
                            cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                        4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
                    else:
                        if (info[3] == 104):
                            cur.execute(SQL4, info[2])
                            tre = cur.fetchall()
                            if (len(tre) == 0):
                                tre = [(0, 0)]
                            if (charge > abs(info[4]) - tre[0][1]):
                                tender = abs(info[4]) - tre[0][1]
                                for bN1 in bN:
                                    bnum.append(bN1[0])
                                miao.append(tender)
                                charge -= abs(info[4]) - tre[0][1]
                                cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                            4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
                            else:
                                tender = charge
                                for bN1 in bN:
                                    bnum.append(bN1[0])
                                miao.append(tender)
                                charge = 0
                                cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                            4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
                        elif (info[3] == 557):
                            cur.execute(SQL5, info[2])
                            business_code = cur.fetchall()
                            cur.execute(SQL4, business_code)
                            tre = cur.fetchall()
                            if (len(tre) == 0):
                                tre = [(0, 0)]
                            if (charge > abs(info[4]) - tre[0][1]):
                                tender = abs(info[4]) - tre[0][1]
                                charge -= abs(info[4]) - tre[0][1]
                                cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                            4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
                            else:
                                tender = charge
                                charge = 0
                                cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                            4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
                        elif (info[3] == 202):
                            cur.execute(SQL4, info[2])
                            tre = cur.fetchall()
                            if (len(tre) == 0):
                                tre = [(0, 0)]
                            if (charge > abs(info[4]) - tre[0][1]):
                                tender = abs(info[4]) - tre[0][1]
                                charge -= abs(info[4]) - tre[0][1]
                                cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                            4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
                            else:
                                tender = charge
                                charge = 0
                                cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                            4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
        # 666还款冻结业务
        elif (info[3] == 666):
            if (charge <= 0):
                charge = 0
                tender = 0
            elif (charge > 0):
                if (charge > info[4]):
                    charge += info[4]
                    tender += info[4]
                    cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
                else:
                    tender = charge
                    charge = 0
                    tender = 0
                    cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))

        # 108获得还款业务（秒标回款）、20053发放现金券业务
        elif (info[3] == 108 or info[3] == 20053):
            if (info[3] == 108):
                cur.execute(SQL3, info[2])
                btype = cur.fetchall()
                for btype1 in btype:
                    if (btype1[0]) == 5:
                        ninemiao = 0
                        for r in range(len(miao)):
                            if (btype1[1] == bnum[r]):
                                ninemiao += abs(miao[r])
                        if (charge <= 0):
                            charge = 0
                            charge += ninemiao
                            tender = 0
                            cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                        4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
                        else:
                            charge += ninemiao
                            tender = 0
                            cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                        4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
            elif (info[3] == 20053):
                cash1 = 0
                for r in range(len(cash)):
                    if (info[2] == cnum[r]):
                        cash1 += abs(cash[r])
                if (charge <= 0):
                    charge = 0
                    charge += cash1
                    tender = 0
                    cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
                else:
                    charge += cash1
                    tender = 0
                    cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))

        # 106撤标(供应链)
        elif(info[3] == 106):
            if (borrow[1] == 5):
                for r in range(len(miao)):
                    if (borrow[5] == bnum[r]):
                        charge += abs(miao[r])
                        tender = 0
                        cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                    4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))

        # 403VIP会员费、999捐款、30001超级会员充值（从新充值扣除）
        elif (info[3] == 403 or info[3] == 999 or info[3] == 30001):
            if (charge <= 0):
                charge = 0
                tender = 0
            elif (charge > 0):
                if (charge >= abs(info[4])):
                    charge += info[4]
                    tender = 0
                    cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
                else:
                    tender = 0
                    charge = 0
                    cur.execute(SQL1, (info[2], userid1[0], info[3], charge, tender, info[
                                4], borrow[0], borrow[2], borrow[3], borrow[1], info[6], borrow[4]))
cur.close()
conn.commit()
conn.close()
print('end')
