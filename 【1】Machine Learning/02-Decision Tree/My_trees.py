#-*- coding:utf-8 -*-
'''
Created on 2018.09.28
Decision Tree Source Code for Machine Learning in Action Ch. 3
@author: Cao Sainan
'''
from math import log
import operator
import numpy as np
import pandas as pd
import sklearn
from sklearn import tree

##### 计算给定数据集的信息熵 ######


def calcShannonEnt(dataSet):
    numEntries = len(dataSet)  # 样本数
    labelCounts = {}   # 创建一个数据字典：key是最后一列的数值（即标签，也就是目标分类的类别），value是属于该类别的样本个数
    for featVec in dataSet:  # 遍历整个数据集，每次取一行
        currentLabel = featVec[-1]  # 取该行最后一列的值
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1  # 统计每种类别的样本数
    shannonEnt = 0.0  # 初始化信息熵
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries  # 计算每种类别的概率
        shannonEnt -= prob * log(prob, 2)  # log base 2  计算信息熵
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
# # 测试calcShannonEnt()函数
myDat, labels = createDataSet()
# print(myDat, '\n', calcShannonEnt(myDat))


##### 按给定的特征划分数据 #########


# axis是dataSet数据集下要进行特征划分的列号，value是该列下某个特征值
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:  # 遍历数据集，并抽取按axis的当前value特征进划分的数据集(不包括axis列的值)
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]  # 创建空列表
            reducedFeatVec.extend(featVec[axis + 1:])  # 将axis之后的列全部加入空列表
            retDataSet.append(reducedFeatVec)
            print(axis, value, reducedFeatVec)
    print(retDataSet)
    return retDataSet
# 测试splitDataSet()函数
# print(splitDataSet(myDat, 0, 0))
# print(splitDataSet(myDat, 0, 1))



##### 选取当前数据集下，用于划分数据集的最优特征 #####


def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1  # 获取当前数据集的特征个数，最后一列是分类标签
    baseEntropy = calcShannonEnt(dataSet)  # 计算当前数据集‘根结点’的信息熵
    bestInfoGain = 0.0  # 初始化最优信息增益
    bestFeature = -1    # 初始化最优的特征
    for i in range(numFeatures):  # 遍历每个特征
        featList = [example[i] for example in dataSet]  # 获取数据集中当前特征下的所有值
        # 获取当前唯一的特征值，例如outlook下有sunny、overcast、rainy
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:  # 计算每种划分方式的信息熵
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))  # 计算分支结点的权重
            newEntropy += prob * calcShannonEnt(subDataSet)  # 每个分支加总的信息熵
        infoGain = baseEntropy - newEntropy  # 计算信息增益
        if (infoGain > bestInfoGain):  # 比较每个特征的信息增益，只要最好的信息增益
            bestInfoGain = infoGain  # if better than current best, set to best
            bestFeature = i
        # print(numFeatures, featList, uniqueVals, subDataSet)
    return bestFeature  # returns an integer
# 测试chooseBestFeatureToSplit()函数
print(chooseBestFeatureToSplit(myDat))


# # 该函数使用分类名称的列表，然后创建键值为classList中唯一值的数据字典。字典
# # 对象的存储了classList中每个类标签出现的频率。最后利用operator操作键值排序字典，
# # 并返回出现次数最多的分类名称


# def majorityCnt(classList):
#     classCount = {}
#     for vote in classList:
#         if vote not in classCount.keys():
#             classCount[vote] = 0
#         classCount[vote] += 1
#     sortedClassCount = sorted(classCount.iteritems(),
#                               key=operator.itemgetter(1), reverse=True)
#     return sortedClassCount[0][0]


# # 生成决策树主方法


# def createTree(dataSet, labels):
#     classList = [example[-1] for example in dataSet]  # 返回当前数据集下标签列所有值
#     if classList.count(classList[0]) == len(classList):
#         return classList[0]  # 当类别完全相同时则停止继续划分，直接返回该类的标签
#     if len(dataSet[0]) == 1:  # 遍历完所有的特征时，仍然不能将数据集划分成仅包含唯一类别的分组 dataSet
#         return majorityCnt(classList)  # 由于无法简单的返回唯一的类标签，这里就返回出现次数最多的类别作为返回值
#     bestFeat = chooseBestFeatureToSplit(dataSet)  # 获取最好的分类特征索引
#     bestFeatLabel = labels[bestFeat]  # 获取该特征的名字

#     # 这里直接使用字典变量来存储树信息，这对于绘制树形图很重要。
#     myTree = {bestFeatLabel: {}}  # 当前数据集选取最好的特征存储在bestFeat中
#     del(labels[bestFeat])  # 删除已经在选取的特征
#     featValues = [example[bestFeat] for example in dataSet]
#     uniqueVals = set(featValues)
#     for value in uniqueVals:
#         # copy all of labels, so trees don't mess up existing labels
#         subLabels = labels[:]
#         myTree[bestFeatLabel][value] = createTree(
#             splitDataSet(dataSet, bestFeat, value), subLabels)
#     return myTree


# def classify(inputTree, featLabels, testVec):
#     firstStr = inputTree.keys()[0]
#     secondDict = inputTree[firstStr]
#     featIndex = featLabels.index(firstStr)
#     key = testVec[featIndex]
#     valueOfFeat = secondDict[key]
#     if isinstance(valueOfFeat, dict):
#         classLabel = classify(valueOfFeat, featLabels, testVec)
#     else:
#         classLabel = valueOfFeat
#     return classLabel


# def storeTree(inputTree, filename):
#     import pickle
#     fw = open(filename, 'w')
#     pickle.dump(inputTree, fw)
#     fw.close()


# def grabTree(filename):
#     import pickle
#     fr = open(filename)
#     return pickle.load(fr)


# if __name__ == '__main__':
#     fr = open('play.tennies.txt')
#     lenses = [inst.strip().split(' ') for inst in fr.readlines()]
#     lensesLabels = ['outlook', 'temperature', 'huminidy', 'windy']
#     lensesTree = createTree(lenses, lensesLabels)
#     treePlotter.createPlot(lensesTree)


# #!/usr/bin/python
# # encoding:utf-8

# import matplotlib.pyplot as plt

# decisionNode = dict(boxstyle="sawtooth", fc="0.8")  # 定义文本框与箭头的格式
# leafNode = dict(boxstyle="round4", fc="0.8")
# arrow_args = dict(arrowstyle="<-")


# def getNumLeafs(myTree):  # 获取树叶节点的数目
#     numLeafs = 0
#     firstStr = myTree.keys()[0]
#     secondDict = myTree[firstStr]
#     for key in secondDict.keys():
#         # 测试节点的数据类型是不是字典，如果是则就需要递归的调用getNumLeafs()函数
#         if type(secondDict[key]).__name__ == 'dict':
#             numLeafs += getNumLeafs(secondDict[key])
#         else:
#             numLeafs += 1
#     return numLeafs


# def getTreeDepth(myTree):  # 获取树的深度
#     maxDepth = 0
#     firstStr = myTree.keys()[0]
#     secondDict = myTree[firstStr]
#     for key in secondDict.keys():
#         # test to see if the nodes are dictonaires, if not they are leaf nodes
#         if type(secondDict[key]).__name__ == 'dict':
#             thisDepth = 1 + getTreeDepth(secondDict[key])
#         else:
#             thisDepth = 1
#         if thisDepth > maxDepth:
#             maxDepth = thisDepth
#     return maxDepth

# # 绘制带箭头的注释


# def plotNode(nodeTxt, centerPt, parentPt, nodeType):
#     createPlot.ax1.annotate(nodeTxt, xy=parentPt,  xycoords='axes fraction',
#                             xytext=centerPt, textcoords='axes fraction',
# va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)

# # 计算父节点和子节点的中间位置，在父节点间填充文本的信息


# def plotMidText(cntrPt, parentPt, txtString):
#     xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
#     yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
#     createPlot.ax1.text(xMid, yMid, txtString, va="center",
#                         ha="center", rotation=30)

# # 画决策树的准备方法


# def plotTree(myTree, parentPt, nodeTxt):  # if the first key tells you what feat was split on
#     numLeafs = getNumLeafs(myTree)  # 计算树的宽度
#     depth = getTreeDepth(myTree)  # 计算树的深度
#     firstStr = myTree.keys()[0]  # the text label for this node should be this
#     cntrPt = (plotTree.xOff + (1.0 + float(numLeafs)) /
#               2.0 / plotTree.totalW, plotTree.yOff)
#     plotMidText(cntrPt, parentPt, nodeTxt)
#     plotNode(firstStr, cntrPt, parentPt, decisionNode)
#     secondDict = myTree[firstStr]
#     plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
#     for key in secondDict.keys():
#         # test to see if the nodes are dictonaires, if not they are leaf nodes
#         if type(secondDict[key]).__name__ == 'dict':
#             plotTree(secondDict[key], cntrPt, str(key))  # recursion
#         else:  # it's a leaf node print the leaf node
#             plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
#             plotNode(secondDict[key], (plotTree.xOff,
#                                        plotTree.yOff), cntrPt, leafNode)
#             plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
#     plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD
# # if you do get a dictonary you know it's a tree, and the first element
# # will be another dict

# # 画决策树主方法


# def createPlot(inTree):
#     fig = plt.figure(1, facecolor='white')
#     fig.clf()
#     axprops = dict(xticks=[], yticks=[])
#     createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)  # no ticks
#     # createPlot.ax1 = plt.subplot(111, frameon=False) #ticks for demo puropses
#     plotTree.totalW = float(getNumLeafs(inTree))
#     plotTree.totalD = float(getTreeDepth(inTree))
#     plotTree.xOff = -0.5 / plotTree.totalW
#     plotTree.yOff = 1.0
#     plotTree(inTree, (0.5, 1.0), '')
#     plt.show()

# # def createPlot():
# #    fig = plt.figure(1, facecolor='white')
# #    fig.clf()
# #    createPlot.ax1 = plt.subplot(111, frameon=False) #ticks for demo puropses
# #    plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
# #    plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
# #    plt.show()


# def retrieveTree(i):
#     listOfTrees = [{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
#                    {'no surfacing': {0: 'no', 1: {'flippers': {
#                        0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}
#                    ]
#     return listOfTrees[i]
