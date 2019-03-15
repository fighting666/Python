# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import operator
import math


# =======================================================================================================
# 1、k-近邻简单分类的应用


# def createDataSet():
#     """
#     构建一组训练数据（训练样本），共4个样本及labels
#     """
#     group = np.array([
#         [1.0, 1.1],
#         [1.0, 1.0],
#         [0., 0.],
#         [0., 0.1]
#     ])
#     labels = ['A', 'A', 'B', 'B']
#     return group, labels


def classify0(inX, dataset, labels, k):
    """
    K-近邻算法核心分类器
    inX 是输入的测试样本，是一个[x, y]样式的
    dataset 是训练样本集，labels 是训练样本标签
    """
    # shape返回矩阵的[行数 shape[0],列数 shape[1]],行数就是样本的数量
    dataSetSize = dataset.shape[0]

    # tile把输入的测试样本扩展为和dataset的shape一样，就可以直接做矩阵减法
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataset

    # diffMat就是输入样本与每个训练样本的差值，对其每个x和y的差值进行平方运算
    sqDiffMat = diffMat ** 2

    # axis=1表示按照横轴，sum表示累加，即按照行进行累加。
    sqDistance = sqDiffMat.sum(axis=1)

    # 对平方和进行开根号
    distance = sqDistance ** 0.5

    # 按照升序进行快速排序，返回的是原数组的下标。
    # 比如，x = [30, 10, 20, 40],升序排序后应该是[10,20,30,40],他们的原下标是[1,2,0,3]
    sortedDistIndicies = distance.argsort()

    # 存放最终的分类结果及相应的结果投票数
    classCount = {}

    # 投票过程，就是统计前k个最近的样本所属类别包含的样本个数
    for i in range(k):
        # index = sortedDistIndicies[i]是第i个最相近的样本下标
        # voteIlabel = labels[index]是样本index对应的分类结果('A' or 'B')
        voteIlabel = labels[sortedDistIndicies[i]]
        # classCount.get(voteIlabel, 0)返回voteIlabel的值，如果不存在，则返回0，然后将票数增1
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

    # 把分类结果进行排序，然后返回得票数最多的分类结果
    sortedClassCount = sorted(
        classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

# # 结果输出
# if __name__ == "__main__":
#     # 导入数据
#     dataset, labels = createDataSet()
#     inX = [0.1, 0.1]
#     # 简单分类
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
    numberOfLines = len(arrayOlines)  # 获取 n=样本的行数
    # 创建一个2维矩阵用于存放训练样本数据，一共有n行，每一行存放3个数据
    returnMat = np.zeros((numberOfLines, 3))
    classLabelVector = []  # 创建一个1维数组用于存放训练样本标签
    index = 0
    for line in arrayOlines:
        # 把回车符号给去掉
        line = line.strip()
        # 把每一行数据用\t分割
        listFromLine = line.split('\t')
        # 把分割好的数据放至数据集，其中index是该样本数据的下标，就是放到第几行
        returnMat[index, :] = listFromLine[0:3]
        # 把该样本对应的标签放至标签集，顺序与样本集对应。
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector

# # 查看file2matrix函数结果
# datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
# print(datingDataMat, datingLabels)
# # 绘制散点图
# fig = plt.figure()
# ax = fig.add_subplot(111)
# #ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], datingDataMat[:, 2])
# # 通过第一、第二个特征属性区分样本所属的类别
# ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1],
#            15.0 * np.array(datingLabels), 15.0 * np.array(datingLabels))
# plt.show()


def autoNorm(dataSet):
    """
    训练数据归一化特征值
    """
    # 获取数据集中每一列的最小、最小数值，以createDataSet()中的数据为例，group.min(0)=[0,0]
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    # 创建一个与dataSet同shape的全0矩阵，用于存放归一化后的数据
    normDataSet = np.zeros(dataSet.shape)
    m = dataSet.shape[0]
    # 把最小值扩充为与dataSet同shape，然后作差
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    # 把最大最小差值扩充为dataSet同shape，然后作商，是指对应元素进行除法运算，而不是矩阵除法。
    # 矩阵除法在numpy中要用linalg.solve(A,B)
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    return normDataSet, ranges, minVals

# # 查看autoNorm函数结果
# normDataSet, ranges, minVals = autoNorm(datingDataMat)
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
        print("KNN分类器预测分类结果: %d, 真实结果: %d, 预测结果的正误: %s" % (
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
    # 交互输入样本的三个特征
    percenTage = float(input("percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    # 读入训练数据集
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
    # 循环读取32行，32列
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32 * i + j] = int(lineStr[j])
    return returnVect

# # 查看转化后的数据
# vect = img2vector('trainingDigits\\0_0.txt')
# print(vect[0, 50:100])


def handwritingClassTest():
    '''
    手写数字识别系统测试代码
    '''
    # 训练数据及样本标签的构造
    hwLabels = []
    # listdir将指定目录文件名存储在列表中
    trainingFileList = listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = np.zeros((m, 1024))  # 创建m*1024训练矩阵,每行是一个图像
    for i in range(m):
        # 从文件名中解析出当前图像的标签，也就是数字是几，文件名格式为 0_3.txt 表示图片数字是 0
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)  # 将类标签存入矩阵
        # 使用img2vector将每个图像文件存成矩阵
        trainingMat[i, :] = img2vector('trainingDigits/%s' % fileNameStr)

    # 测试数据构造及执行分类器
    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)

        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print("KNN分类器预测分类结果: %d,  真实结果: %d, 预测结果的正误: %s" % (
            classifierResult, classNumStr, classifierResult == classNumStr))
        if (classifierResult != classNumStr):
            errorCount += 1.0
    print("\nthe total number of errors is: %d / %d" % (errorCount, mTest))
    print("\nthe total error rate is: %f" % (errorCount / float(mTest)))

# 打印预测结果
print(handwritingClassTest())

# =======================================================================================================
# 4、使用scikit-learn实现KNN算法
"""
scikit-learn 库对knn的支持
数据集是iris虹膜数据集
"""

from sklearn.datasets import load_iris
from sklearn import neighbors
import sklearn

# 查看iris数据集
iris = load_iris()
# print(iris)

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
# knn = neighbors.KNeighborsClassifier()
# # 训练数据集
# knn.fit(iris.data, iris.target)
# # 训练准确率
# score = knn.score(iris.data, iris.target)

# # 预测
# predict = knn.predict([[0.1, 0.2, 0.3, 0.4]])
# # 预测，返回概率数组
# predict2 = knn.predict_proba([[0.1, 0.2, 0.3, 0.4]])

# print(predict)
# print(iris.target_names[predict])


# =======================================================================================================
# tile属于numpy模块下边的函数
# tile（A, reps）返回一个shape=reps的矩阵，矩阵的每个元素是A
# 比如 A=[0,1,2] 那么，tile(A, 2)= [0, 1, 2, 0, 1, 2]
# tile(A,(2,2)) = [[0, 1, 2, 0, 1, 2],
#                  [0, 1, 2, 0, 1, 2]]
# tile(A,(2,1,2)) = [[[0, 1, 2, 0, 1, 2]],
#                    [[0, 1, 2, 0, 1, 2]]]
# 上边那个结果的分开理解就是：
# 最外层是2个元素，即最外边的[]中包含2个元素，类似于[C,D],而此处的C=D，因为是复制出来的
# 然后C包含1个元素，即C=[E],同理D=[E]
# 最后E包含2个元素，即E=[F,G],此处F=G，因为是复制出来的
# F就是A了，基础元素
# 综合起来就是(2,1,2)= [C, C] = [[E], [E]] = [[[F, F]], [[F, F]]] = [[[A, A]], [[A, A]]]
# 这个地方就是为了把输入的测试样本扩展为和dataset的shape一样，然后就可以直接做矩阵减法了。
# 比如，dataset有4个样本，就是4*2的矩阵，输入测试样本肯定是一个了，就是1*2，为了计算输入样本与训练样本的距离
# 那么，需要对这个数据进行作差。这是一次比较，因为训练样本有n个，那么就要进行n次比较；
# 为了方便计算，把输入样本复制n次，然后直接与训练样本作矩阵差运算，就可以一次性比较了n个样本。
# 比如inX = [0,1],dataset就用函数返回的结果，那么
# tile(inX, (4,1))= [[ 0.0, 1.0],
#                    [ 0.0, 1.0],
#                    [ 0.0, 1.0],
#                    [ 0.0, 1.0]]
# 作差之后
# diffMat = [[-1.0,-0.1],
#            [-1.0, 0.0],
#            [ 0.0, 1.0],
#            [ 0.0, 0.9]]
