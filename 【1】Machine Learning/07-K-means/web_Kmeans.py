# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import random
import re
import os
import matplotlib.pyplot as plt
"""
def loadDataSet()    输入：样本集
def distEclud()      计算样本欧式距离
def initCentroids()  从样本集中随机选择k个样本作为初始向量，即k个初始质心点
def minDistance()    计算当前数据与k个质心之间的距离,将当前数据加入到距离其最近的簇
def getCentroids()   对于每个簇，计算其均值，即得到新的k个质心点
def getVar()         连续两次迭代的均方误差小于0.0001
"""


def loadDateSet(filename):
    dataSet = []
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split('\t')  # 以空白符为分割，并删除首、尾处的空白符
        fltLine = map(float, curLine)  # map函数将curLine中的所有元素都转化成float
        dataSet.append(fltLine)  # 向空列表dataMat中追加元素
    return dataSet

filename = "data\\testSet.txt"  # 数据文件
dataSet = loadDateSet(filename)  # 载入数据集


def distEclud(vec1, vec2):
    """
    计算向量vec1和vec2之间的距离
    """
    return np.sqrt(np.sum(np.square(vec1 - vec2)))
    # return sqrt(sum(power(vec1 - vec2, 2)))


def initCentroids(dataSet, k):
    """
    初始化k个质心，随机获取
    """
    return random.sample(dataSet, k)  # 从dataSet中随机获取k个数据项返回


def minDistance(dataSet, centroidList):
    """
    对每个属于dataSet的item，计算item与centroidList中k个质心的欧式距离，
    找出距离最小的,并将item加入相应的簇类中
    """
    clusterDict = dict()  # 用dict来保存簇类的结果
    for item in dataSet:
        vec1 = np.array(item)  # 转换成array的形式
        flag = 0  # 簇分类标记，记录与相应簇距离最近的那个簇
        minDis = float("inf")  # 初始化为最大值

        for i in range(len(centroidList)):
            vec2 = np.array(centroidList[i])
            distance = distEclud(vec1, vec2)  # 计算相应的欧式距离
            if distance < minDis:
                minDis = distance
                flag = i  # 循环结束时，flag保存的是与当前item距离最近的那个簇标记

        if flag not in clusterDict.keys():  # 簇标记不存在，进行初始化
            clusterDict[flag] = list()  # print falg,item
            clusterDict[flag].append(item)  # 加入相应的类别中

    return clusterDict  # 返回新的聚类结果

print clusterDict


# def getCentroids(clusterDict):
#     """
#     得到k个质心
#     """
#     centroidList = list()
#     for key in clusterDict.keys():
#         centroid = np.mean(np.array(
#             clusterDict[key]), axis=0)  # 计算每列的均值，找到质心
#         # print key,centroid
#         centroidList.append(centroid)

#     return np.array(centroidList).tolist()


# def getVar(clusterDict, centroidList):
#     """
#     计算簇集合之间的均方差
#     将簇类中各个向量与质心的距离进行累加求和
#     """
#     sum = 0.0
#     for key in clusterDict.keys():
#         vec1 = np.array(centroidList[key])
#         distance = 0.0
#         for item in clusterDict[key]:
#             vec2 = np.array(item)
#             distance += distEclud(vec1, vec2)
#         sum += distance
#     return sum


# def showCluster(centroidList, clusterDict):
#     """
#     可视化展示
#     """
#     colorMark = ['or', 'ob', 'og', 'ok', 'oy', 'ow']
#     centroidMark = ['dr', 'db', 'dg', 'dk', 'dy', 'dw']
#     for key in clusterDict.keys():
#         plt.plot(centroidList[key][0], centroidList[key]
#                  [1], centroidMark[key], markersize=12)
#         for item in clusterDict(key):
#             plt.plot(item[0], item[1], colorMark[key])

#     plt.show()


# if __name__ == '__main__':

#     filename = "data\\testSet.txt"  # 数据文件
#     dataSet = loadDateSet(filename)  # 载入数据集
#     centroidList = initCentroids(dataSet, 4)  # 初始化质心。k=4
#     clusterDict = minDistance(dataSet, centroidList)  # 第一次聚类迭代
#     newVar = getVar(clusterDict, centroidList)  # 获取均方误差值，通过新旧均方误差来获得迭代终止条件
#     oldvar = -0.0001  # 旧的均方误差值初始化为-1

#     print '*****第一次迭代*******'
#     print
#     print '簇类'
#     for key in clusterDict.keys():
#         print key, '-->', clusterDict[key]
#     print 'k个均值向量：', centroidList
#     print '平方均方误差：', newVar
#     print
#     showCluster(centroidList, clusterDict)  # 展示聚类结果

#     n = 2
#     while ads(newVar - oldvar) >= 0.0001:  # 当连续两次聚类结果小于0.0001时，迭代结束
#         centroidList = getCentroids(clusterDict)  # 获得新的质心
#         clusterDict = minDistance(dataSet, centroidList)
#         oldvar = newVar
#         newVar = getVar(clusterDict, centroidList)

#         print '*****第%d次迭代*****' % n
#         print
#         print '簇类'
#         for key in clusterDict.keys():
#             print key, '-->', clusterDict[key]
#         print 'k个均值向量：', centroidList
#         print '平均均方误差：', newVar
#         print
#         showCluster(centroidList, clusterDict)

#         n += 1
