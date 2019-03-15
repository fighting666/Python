#-*- coding:utf-8 -*-
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os


def loadDataSet():
    '''
    生成数据集dataset
    '''
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]


def createC1(dataSet):
    '''
    输出数据集的所有项，数据中出现的元素都存入c1中
    '''
    C1 = []
    for transction in dataSet:
        for item in transction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return map(frozenset, C1)  # 冻结c1中的元素


def scanD(D, Ck, minSupport):
    '''
    # 该函数用于从 C1 生成 L1
    DataSet为输入的数据集（事务集）
    ck的每个项集为frozenset型数据，为DataSet所有项的唯一值，候选频繁项集minSupport为设定的最小支持度
    功能：从候选项集中找出支持度support大于minSupport的频繁项集
    输出：频繁项集集合returnList,以及频繁项集对应的支持度support
    '''
    subSetCount = {}
    # 取出数据集dataset中的每行记录
    for tid in D:
        # 取出候选频繁项集ck中的每个项集
        for can in Ck:
            # 判断ck中的每个项集是否为数据集dataset中的子集
            if can.issubset(tid):
                # 如果是dataset的子集，就增加freqSetCount的计数
                if not subSetCount.has_key(can):
                    subSetCount[can] = 1
                else:
                    subSetCount[can] += 1
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in subSetCount:
        support = subSetCount[key] / numItems  # 计算支持度
        # print key,freqSetCount[key],support
        # 选出大于最小支持度的频繁项集
        if support >= minSupport:
            retList.insert(0, key)  # 满足条件加入L1中
            supportData[key] = support
    return retList, supportData


def createCk(Lk, k):
    '''
    输入为：频繁项集列表Lk和项集元素个数k
    输出为：频繁项集Lk组合后的唯一的频繁项集ck
    '''
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):  # 比较Lk中的每一个元素和其他元素
        for j in range(i + 1, lenLk):
            L1 = list(Lk[i])[:k - 2]
            L2 = list(Lk[j])[:k - 2]
            # print j, list(Lk[i]), L1, list(Lk[j]), L2
            L1.sort()
            L2.sort()
            if L1 == L2:
                # 取列表中两个集合比较，如果这两个集合的前k-2个元素相等，就将这两个集合合并成一个大小为k的集合，比较集合{0,1}{0,2}{1,2}的第1个元素并只对第1个元素相同的集合求并
                retList.append(Lk[i] | Lk[j])
    return retList

# print createCk(([frozenset([2, 3, 5])]), 4)


def apriori(dataSet, minSupport=0.5):
    C1 = createC1(dataSet)  # 产生候选频繁项集的列表
    D = map(set, dataSet)  # 事务集
    L1, supportData = scanD(D, C1, minSupport)
    # 由c1产生大于最小支持度的候选项集L1
    # print c1, DataSet, L1, returnsupportData
    L = [L1]  # L包含L1,L2,L3...,现在有L1，后面陆续找到L2，L3
    k = 2
    # print L, L[k - 2], len(L[k - 2])
    while (len(L[k - 2]) > 0):
        Ck = createCk(L[k - 2], k)  # 根据L创建ck
        # print ck
        # 基于ck创建Lk，将满足最下支持度的Lk添加到L中
        Lk, supportLk = scanD(D, Ck, minSupport)
        supportData.update(supportLk)
        L.append(Lk)
        k += 1  # 逐一增加频繁项集中的元素个数
    return L, supportData  # 当Lk为空时，返回L并退出

#------------------关联规则生成函数--------------#


def generateRules(L, supportData, minConference=0.7):
    # apriori产生的频繁项集和具有支持度的字典，最小可信度
    bigRuleList = []  # 存储所有的关联规则
    for i in range(1, len(L)):
        # 从1,即第二个元素开始，L[0]是单个元素的,两个及以上的才可能有关联一说，单个元素的项集不存在关联问题
        for freqSet in L[i]:
            # 遍历L中的每一个频繁项集并对每个频繁项集创建只包含单个元素集合的列表H1
            H1 = [frozenset([item]) for item in freqSet]
            # print freqSet,H1
            if (i > 1):  # 如果频繁项集元素数目超过2,那么会考虑对它做进一步的合并
                rulesFromConseq(freqSet, H1, supportData,
                                bigRuleList, minConference)
            else:  # 第一层时，后件数为1
                calculationConf(freqSet, H1, supportData,
                                bigRuleList, minConference)
    return bigRuleList


def calculationConf(freqSet, H, supportData, brl, minConference=0.7):
    '''
    生成候选规则集合：计算规则的可信度以及找到满足最小可信度要求的规则,针对项集中只有两个元素时，计算可信度
    '''
    prunedH = []  # 返回一个满足最小可信度要求的规则列表
    for conseq in H:  # 后件，遍历H中的所有项集并计算可信度值
        conf = supportData[freqSet] / \
            supportData[freqSet - conseq]
    if conf >= minConference:
        print freqSet - conseq, '-->', conseq, 'conf:', conf
        brl.append((freqSet - conseq, conseq, conf))
        prunedH.append(conseq)

    return prunedH


def rulesFromConseq(freqSet, H, supportData, brl, minConference=0.7):
    m = len(H[0])
    # 频繁项集元素数目大于单个集合的元素数
    if (len(freqSet) > (m + 1)):
        # 利用函数createCk生成包含m+1个元素的候选频繁项集后件
        Hmp1 = createCk(H, (m + 1))
        Hmp1 = calculationConf(freqSet, Hmp1, supportData, brl, minConference)
        # 当候选后件集合中只有一个后件的可信度大于最小可信度，则结束递归创建规则
        if (len(Hmp1) > 1):
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConference)

L, suppData = apriori(loadDataSet(), minSupport=0.5)
# print L, suppData
rule = generateRules(L, suppData, minConference=0.7)
print rule
# [[frozenset([1]), frozenset([3]), frozenset([2]), frozenset([5])],  0
# [frozenset([1, 3]), frozenset([2, 5]), frozenset([2, 3]), frozenset([3, 5])],   1
# [frozenset([2, 3, 5])],   2
# []]   3

# {frozenset([5]): 0.75,
#  frozenset([3]): 0.75,
#  frozenset([2, 3, 5]): 0.5,
#  frozenset([3, 5]): 0.5,
#  frozenset([2, 3]): 0.5,
#  frozenset([2, 5]): 0.75,
#  frozenset([1]): 0.5,
#  frozenset([1, 3]): 0.5,
#  frozenset([2]): 0.75}

# frozenset([1, 3]) [frozenset([1]), frozenset([3])]
# frozenset([2, 5]) [frozenset([2]), frozenset([5])]
# frozenset([2, 3]) [frozenset([2]), frozenset([3])]
# frozenset([3, 5]) [frozenset([3]), frozenset([5])]
# frozenset([2, 3, 5]) [frozenset([2]), frozenset([3]), frozenset([5])]
