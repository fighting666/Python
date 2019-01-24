# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import math
import matplotlib as plt
import scipy


# vec1 = np.array([1, 2, 3])
# vec2 = np.array([4, 5, 6])
# str1 = np.array([1, 1, 0, 1, 0, 1, 0, 0, 1])
# str2 = np.array([0, 1, 1, 0, 0, 0, 1, 1, 1])

# # (1)Euclidean1,欧式距离的计算

# def Euclidean1(vec1, vec2):
#     return np.sqrt(np.sum(np.square(vec1 - vec2)))

# def Euclidean2(vec1, vec2):
#     return math.sqrt(((vec1 - vec2)**2).sum())

# # def Euclidean3(vec1, vec2):
# #     return math.sqrt(sum(power(vec1 - vec2, 2)))

# # def Euclidean4(vec1, vec2):
# #     return math.sqrt((vec1 - vec2) * ((vec1 - vec2).T))

# print Euclidean1(vec1, vec2)
# print Euclidean2(vec1, vec2)
# # print Euclidean3(vec1, vec2)
# # print Euclidean4(vec1, vec2)

# #---------------------------------------------------------------------------------------------------------------------
# # (2)Manhattan,曼哈顿距离计算

# def Manhattan1(vec1, vec2):
#     return np.abs((vec1 - vec2)).sum()

# def Manhattan2(vec1, vec2):
#     return sum(abs(vec1 - vec2))

# print Manhattan1(vec1, vec2)
# print Manhattan2(vec1, vec2)

# #---------------------------------------------------------------------------------------------------------------------
# #(3)Chebyshev,切比雪夫距离

# def Chebyshev(vec1, vec2):
#     return max(abs(vec1 - vec2))
#     return np.abs(vec1 - vec2).max()

# print Chebyshev(vec1, vec2)

# #---------------------------------------------------------------------------------------------------------------------
# # (4)MinkowskiDistance 闵可夫斯基距离，其实就是上面三种距离的集合，这里就不重复了。

# def Minkowski(vec1, vec2, params):
#     pass

# #---------------------------------------------------------------------------------------------------------------------
# # (5)Standardized Euclidean distance,标准化欧氏距离
# # 在对长方体区域进行聚类的时候，普通的距离无法满足要求。
# # 按照普通的距离聚类出的大多是圆形的区域，这时候要采用标准的欧式距离。

# # def Standardized_Euclidean(vec1, vec2, v):
# #     npvec = np.array([vec1, vec2])
# #     return spatial.distance.pdist(npvec, 'seuclidean', V=None)

# #---------------------------------------------------------------------------------------------------------------------
# # (6)Mahalanobis,马氏距离

# # def Mahalannobis(vec1, vec2):
# #     npvec = np.array([vec1, vec2])
# #     sub = npvec.T[0] - npvec.T[1]  # 矩阵的转置
# #     inv_sub = np.linalg.inv(np.cov(vec1, vec2))  # 协方差矩阵的逆
# #     return math.sqrt(np.dot(inv_sub, sub).dot(sub.T))

# # print Mahalannobis(vec1, vec2)

# #---------------------------------------------------------------------------------------------------------------------
# # (7)Cosine，余弦夹角
# def Cosine1(vec1, vec2):
# return vec1.dot(vec2) / (math.sqrt((vec1**2).sum())) *
# (math.sqrt((vec2**2).sum()))

# print Cosine1(vec1, vec2)


# def Cosine2(vec1, vec2):
#     return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# print Cosine2(vec1, vec2)

# #---------------------------------------------------------------------------------------------------------------------
# #(8)Hamming distance,汉明距离
# # Levenshtein distance,编辑距离，用于计算两个字符串之间的编辑距离，传入参数为两个字符串

# # str1 = np.mat([[1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 1, 0, 0, 0, 1, 1, 1]])
# # smstr = np.nonzero(str1[0] - str1[1])
# # print np.shape(smstr[0])[1]


# # def Edit_distance_str(str1, str2):
# #     import Levenshtein
# #     edit_distance_distance = Levenshtein.distance(str1, str2)
# #     similarity = 1 - (edit_distance_distance / max(len(str1), len(str2)))
# #     return {'Distance': edit_distance_distance, 'Similarity': similarity}

# # print Edit_distance_str(str1,str2)

# # 针对列表改写的编辑距离，在NLP领域中，计算两个文本的相似度，是基于句子中词和词之间的差异。
# # 如果使用传统的编辑距离算法，则计算的为文本中字与字之间的编辑次数。这里根据编辑距离的思维，
# # 将编辑距离中的处理字符串中的字符对象，变成处理list中每个元素
# def Edit_distance_array(str_ary1, str_ary2):
#     len_str_ary1 = len(str_ary1) + 1
#     len_str_ary2 = len(str_ary2) + 1
#     matrix = [0 for n in range(len_str_ary1 * len_str_ary2)]
#     for i in range(len_str_ary1):
#         matrix[i] = i
#     for j in range(0, len(matrix), len_str_ary1):
#         if j % len_str_ary1 == 0:
#             matrix[j] = j // len_str_ary1
#     for i in range(1, len_str_ary1):
#         for j in range(1, len_str_ary2):
#             if str_ary1[i - 1] == str_ary2[j - 1]:
#                 cost = 0
#             else:
#                 cost = 1
#             matrix[j * len_str_ary1 + i] = min(matrix[(j - 1) * len_str_ary1 + i] + 1, matrix[
#                                                j * len_str_ary1 + (i - 1)] + 1, matrix[(j - 1) * len_str_ary1 + (i - 1)] + cost)
#     distance = int(matrix[-1])
#     similarity = 1 - int(matrix[-1]) / max(len(str_ary1), len(str_ary2))
#     return {'Distance': distance, 'Similarity': similarity}
# #---------------------------------------------------------------------------------------------------------------------
from scipy.spatial.distance import pdist
x = np.random.random(10)
y = np.random.random(10)

# （1）欧氏距离
# 方法一：根据公式求解
d1 = np.sqrt(np.sum(np.square(x - y)))
# 方法二：根据scipy库求解
X = np.vstack([x, y])
d2 = pdist(X)

print d1, d2

# （2）曼哈顿距离
# 方法一：根据公式求解
d1 = np.sum(np.abs(x - y))
# 方法二：根据scipy库求解
X = np.vstack([x, y])
d2 = pdist(X, 'cityblock')

print d1, d2

# (3)切比雪夫距离
# 方法一：根据公式求解
d1 = np.max(np.abs(x - y))
# 方法二：根据scipy库求解
X = np.vstack([x, y])
d2 = pdist(X, 'chebyshev')

print d1, d2

# (4)标准化欧氏距离
# 方法一：根据公式求解
X = np.vstack([x, y])
sk = np.var(X, axis=0, ddof=1)  # 标准化
d1 = np.sqrt(((x - y) ** 2 / sk).sum())
# 方法二：根据scipy库求解
d2 = pdist(X, 'seuclidean')

print d1, d2

#(5)马氏距离
# 马氏距离要求样本数要大于维数，否则无法求协方差矩阵
# 此处进行转置，表示10个样本，每个样本2维
X = np.vstack([x, y])
XT = X.T

# 方法一：根据公式求解
S = np.cov(X)  # 两个维度之间协方差矩阵
SI = np.linalg.inv(S)  # 协方差矩阵的逆矩阵
# 马氏距离计算两个样本之间的距离，此处共有10个样本，两两组合，共有45个距离。
n = XT.shape[0]
d1 = []
for i in range(0, n):
    for j in range(i + 1, n):
        delta = XT[i] - XT[j]
        d = np.sqrt(np.dot(np.dot(delta, SI), delta.T))
        d1.append(d)
# 方法二：根据scipy库求解
from scipy.spatial.distance import pdist
d2 = pdist(XT, 'mahalanobis')
