import numpy as np
import pandas as pd
from math import log

##### 计算给定数据集的信息熵 ######


def calcShannonEnt(dateSet):
    numEntries = len(dateSet)
    labelCounts = {}
    for featVec in dateSet:
        currentLable = featVec[-1]
        if currentLable not in labelCounts.keys():
            labelCounts[currentLable] = 0
        labelCounts[currentLable] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


##### 测试数据用来测试熵的计算 ######


def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no', 'yes']
    return dataSet, labels
# # 测试gain()函数
myDat, labels = createDataSet()
# print(myDat, '\n', gain(myDat))

##### 按给定的特征划分数据 #########


def splitDataSet(dateSet, axis, value):
    retDataSet = []
    for featVec in dateSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)
          # print(axis, value, reducedFeatVec)
    # print(retDataSet)
    return retDataSet
# # 测试splitDataSet()函数
# print(splitDataSet(myDat, 0, 0))
# print(splitDataSet(myDat, 0, 1))

##### 选取当前数据集下，用于划分数据集的最优特征 #####


def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature
# # 测试chooseBestFeatureToSplit()函数
print(chooseBestFeatureToSplit(myDat))
