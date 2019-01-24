#-*- coding:utf-8 -*-
"""
创建于2017.06.13
K-means聚类分析
"""
# from numpy import *
# from pandas import *
'''
def loadDateSet()  输入数据集
def distEclud()    计算样本的欧氏距离
def randCent()     为给定数据集构建一个包含K个随机质心的集合
def kMeans()       k-means聚类算法
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def loadDateSet(filename):
    dataMat = []
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split('\x01')  # 以空白符为分割，并删除首、尾处的空白符
        # fltLine = map(float, curLine)  # map函数将curLine中的所有元素都转化成float
        dataMat.append(curLine)  # 像空列表dataMat中追加元素
    return dataMat


def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))


def randCent(dataSet, k):
    n = shape(dataSet)[1]  # 计算列个数
    centroids = mat(zeros((k, n)))  # 创建一个k*n价的零矩阵
    for j in range(n):
        minJ = min(dataSet[:, j])  # 找到每一维的最小值
        rangeJ = float(max(dataSet[:, j]) - minJ)  # 找到每一维的最大值
        # random.rand(3,2)生成3行2列的随机数
        centroids[:, j] = mat(minJ + rangeJ * random.rand(k, 1))
    return centroids

# 检查前两个函数能否正常运行
dataMat = mat(loadDateSet('data\\testSet.txt'))
print '-*-' * 10
print dataMat
print '-*-' * 10
print randCent(dataMat, 2)
print '-*-' * 10
print distEclud(dataMat[0], dataMat[1])


def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = shape(dataSet)[0]  # 计算行个数（样本个数）
    # 创建一个零矩阵来存储每个点的簇分配结果，一列记录簇索引，第二列存储当前点到簇质心的距离，使用该误差来评价聚类效果
    clusterAssment = mat(zeros((m, 2)))
    centroids = createCent(dataSet, k)  # 初始化K个随机质心的集合
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf
            minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j, :], dataSet[i, :])
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist**2
        print centroids
        for cent in range(k):
            ptsInClust = dataSet[nonzero(clusterAssment[:, 0].A == cent)[0]]
            centroids[cent, :] = mean(ptsInClust, axis=0)
    return centroids, clusterAssment


dataMat = mat(loadDateSet('testSet.txt'))
print kMeans(dataMat, 4)
