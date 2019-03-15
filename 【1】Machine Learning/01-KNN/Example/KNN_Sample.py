#-*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import operator

# =======================================================================================================
# 1、k-近邻简单分类的应用


def createDataSet():
    group = np.array([
        [1.0, 1.1],
        [1.0, 1.0],
        [0., 0.],
        [0., 0.1]
    ])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataset, labels, k):
    '''
    K-近邻算法核心分类器
    '''
    dataSetSize = dataset.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataset
    sqDiffMat = diffMat ** 2
    sqDistance = sqDiffMat.sum(axis=1)
    distance = sqDistance ** 0.5
    sortedDistIndicies = distance.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(
        classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

# # 结果输出
# if __name__ == "__main__":
#     dataset, labels = createDataSet()
#     inX = [0.1, 0.1]
#     className = classify0(inX, dataset, labels, 3)
#     print('测试样本的分类结果是 %s' % className)

# =======================================================================================================
# 2、在约会网站上使用k-近邻算法


def file2matrix(filename):
    """
    从文件中读入训练数据，并存储为矩阵
    """
    fr = open(filename)
    arrayOlines = fr.readlines()
    numberOfLines = len(arrayOlines)
    returnMat = np.zeros((numberOfLines, 3))

    classLabelVector = []
    index = 0
    for line in arrayOlines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector

# # 查看file2matrix函数结果
# datingDataMat,datingLabels=file2matrix('datingTestSet2.txt')
# print(datingDataMat,datingLabels)
# # 绘制散点图
# fig = plt.figure()
# ax = fig.add_subplot(111)
# #ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], datingDataMat[:, 2])
# ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1],
#            15.0 * np.array(datingLabels), 15.0 * np.array(datingLabels))
# plt.show()


def autoNorm(dataset):
    """
    训练数据归一化特征值
    """
    minVals = dataset.min(0)
    maxVals = dataset.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(dataset.shape)
    m = dataset.shape[0]
    normDataSet = dataset - np.tile(minVals, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    return normDataSet, ranges, minVals

# # 查看autoNorm函数结果
# normDataSet, ranges, minVals=autoNorm(datingDataMat)
# print(normDataSet, ranges, minVals)


def datingClassTest():
    '''
    构造约会测试数据及测试分类器
    '''
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[
                                     numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print("KNN分类器预测分类结果: %d, 真实结果: %d, 预测结果的正误 :%s" % (
            classifierResult, datingLabels[i], classifierResult == datingLabels[i]))
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
    print("总错误率是: %f" % (errorCount / float(numTestVecs)))
    print(errorCount)

# # 执行分类器测试数据结果
# print(datingClassTest())


def classifyPerson():
    '''
    构建完整可交互系统，约会网站预测数据
    '''
    resultList = ['not at all', 'in small doses', 'in large doses']
    percenTage = float(input("percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = np.array([ffMiles, percenTage, iceCream])
    classifierResult = classify0(
        (inArr - minVals) / ranges, normMat, datingLabels, 3)
    print("You will probably like this person:",
          resultList[classifierResult - 1])
# print(classifyPerson())


# =======================================================================================================
# 3、手写识别系统实例
from os import listdir


def img2vector(filename):
    """
    将一个32x32的二进制图像矩阵转换为1x1024向量
    """
    returnVect = np.zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32 * i + j] = int(lineStr[j])
    return returnVect

# # 查看转化后的数据
# vect = img2vector('trainingDigits\\0_0.txt')
# print vect[0, 50:100]


def handwritingClassTest():
    '''
    手写数字识别系统测试代码
    '''
    # 训练数据及样本标签的构造
    hwLabels = []
    trainingFileList = listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = np.zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('trainingDigits\\%s' % fileNameStr)

    # 测试数据构造及执行分类器
    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits\\%s' % fileNameStr)

        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print("KNN分类器预测分类结果: %d, 真实结果: %d, 预测结果的正误: %s" % (
            classifierResult, classNumStr, classifierResult == classNumStr))
        if (classifierResult != classNumStr):
            errorCount += 1.0
    print("\n测试样本分类错误的样本数: %d / %d" % (errorCount, mTest))
    print("\n测试样本总错误率是: %f" % (errorCount / float(mTest)))

# 打印预测结果
print(handwritingClassTest())


# =======================================================================================================
# 4、使用scikit-learn实现KNN算法
'''
KNeighborsClassifier(n_neighbors=5, weights='uniform',
                     algorithm='auto', leaf_size=30,
                     p=2, metric='minkowski',
                     metric_params=None, n_jobs=1, **kwargs)
n_neighbors: 默认值为5，表示查询k个最近邻的数目
algorithm:   {‘auto’, ‘ball_tree’, ‘kd_tree’, ‘brute’},指定用于计算最近邻的算法，auto表示试图采用最适合的算法计算最近邻
leaf_size:   传递给‘ball_tree’或‘kd_tree’的叶子大小
metric:      用于树的距离度量。默认'minkowski与P = 2（即欧氏度量）
n_jobs:      并行工作的数量，如果设为-1，则作业的数量被设置为CPU内核的数量
'''
# from sklearn.datasets import load_iris
# from sklearn import neighbors
# import sklearn

# iris = load_iris()
# # print(iris)

# knn = neighbors.KNeighborsClassifier()
# # 训练数据集
# knn.fit(iris.data, iris.target)
# # 训练准确率
# score = knn.score(iris.data, iris.target)
# # 预测
# predict = knn.predict([[0.1, 0.2, 0.3, 0.4]])
# # 预测返回概率数组
# predict2 = knn.predict_proba([[0.1, 0.2, 0.3, 0.4]])
# print(predict)
# print(iris.target_names[predict])
