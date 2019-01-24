#-*- coding:utf-8 -*-
from numpy import *


def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]


def createC1(dataSet):
    '''
    输出数据集的所有项，数据中出现的元素都存入c1中
    '''
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return map(frozenset, C1)


def scanD(D, Ck, minSupport):
    '''
    # 该函数用于从 C1 生成 L1
    DataSet为输入的数据集（事务集）
    ck的每个项集为frozenset型数据，为DataSet所有项的唯一值，候选频繁项集minSupport为设定的最小支持度
    功能：从候选项集中找出支持度support大于minSupport的频繁项集
    输出：频繁项集集合returnList,以及频繁项集对应的支持度support
    '''
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if not ssCnt.has_key(can):
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key] / numItems
        if support >= minSupport:
            retList.insert(0, key)
        supportData[key] = support
    return retList, supportData


def aprioriGen(Lk, k):
    '''
    输入为：频繁项集列表Lk和项集元素个数k
    输出为：频繁项集Lk组合后的唯一的频繁项集ck
    '''
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            L1 = list(Lk[i])[:k - 2]
            L2 = list(Lk[j])[:k - 2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])
    return retList


def apriori(dataSet, minSupport=0.5):
    C1 = createC1(dataSet)
    D = map(set, dataSet)
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while (len(L[k - 2]) > 0):
        Ck = aprioriGen(L[k - 2], k)
        Lk, supK = scanD(D, Ck, minSupport)
        supportData.update(supK)
        L.append(Lk)
        k += 1
    return L, supportData

# print apriori(loadDataSet(), minSupport=0.5)

#---------------------关联规则生成函数---------------------#


def generateRules(L, supportData, minConf=0.7):
    bigRuleList = []
    for i in range(1, len(L)):
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if (i > 1):
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList


def calcConf(freqSet, H, supportData, brl, minConf=0.7):
    '''
    生成候选规则集合：计算规则的可信度以及找到满足最小可信度要求的规则,针对项集中只有两个元素时，计算可信度
    '''
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet] / supportData[freqSet - conseq]
        if conf >= minConf:
            print freqSet - conseq, '-->', conseq, 'conf:', conf
            brl.append((freqSet - conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH


def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
    m = len(H[0])
    if (len(freqSet) > (m + 1)):
        Hmp1 = aprioriGen(H, m + 1)
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf=0.7)
        if (len(Hmp1) > 1):
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf=0.7)

L, suppData = apriori(loadDataSet(), minSupport=0.5)
rule = generateRules(L, suppData, minConf=0.6)
print rule

#------------------发现毒蘑菇的相似特性-------------------#

# mushDateSet = [line.split() for line in open('mushroom.dat').readlines()]
# L, suppData = apriori(mushDateSet, minSupport=0.4)
# for item in L[3]:
#     if item.intersection('2'):
#         print(item)

#------------------发现国会投票模式-------------------#
# from votesmart import votesmart
# from time import sleep
# votesmart.apikey = 'a7fa40adec6f4a77178799fae4441030'


# def getActionIds():
#     actionIdList = []
#     billTitleList = []
#     fr = open('recent20bills.txt')
#     for line in fr.readlines():
#         billNum = int(line.split('\t')[0])
#         try:
#             billDetail = votesmart.votes.getBill(billNum)
#             for action in billDetail.actions:
#                 if action.level == 'House' and (action.stage == 'Passage' or action.stage == 'Amendment Vote'):
#                     actionId = int(action.actionId)
#                     print 'bill: %d has actionId: %d' % (billNum, actionId)
#                     actionIdList.append(actionId)
#                     billTitleList.append(line.strip().split('\t')[1])
#         except:
#             print "problem getting bill %d" % billNum
#         sleep(1)
#     return actionIdList, billTitleList


# print getActionIds()
