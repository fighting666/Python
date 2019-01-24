import cx_Oracle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics

conn3 = cx_Oracle.connect(
    "dafy_analysis/AnalYSIs_df$201801@rptdb01.dafycredit.com:1521/rptdb01")

cur = conn3.cursor()  # sql = "select * from dafy_sales.cross_active_list"
sql = "select deduct_cnt,wx_cnt from wf_table_count where deduct_cnt is not null and wx_cnt is not null and rownum <= 100000"

result = cur.execute(sql)
rs = result.fetchall()
X = np.array(rs).reshape(len(rs), 2)

clf = KMeans(n_clusters=3)    
y_pred = clf.fit_predict(X)    
print(clf)     
print(y_pred) 
x = [n[0] for n in X]    
y = [n[1] for n in X]     
plt.scatter(x, y, c=y_pred, marker='x')     
plt.title("Kmeans-Basketball Data")     
plt.xlabel("assists_per_minute")    
plt.ylabel("points_per_minute")    
plt.legend(["Rank"]) 

# plt.figure(figsize=(8,10))
# plt.subplot(3,2,1)
# x1 = np.array([1, 2, 3, 1, 5, 6, 5, 5, 6, 7, 8, 9, 7, 9])
# x2 = np.array([1, 3, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 1, 3])
# X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)
# plt.xlim([0,10])
# plt.ylim([0,10])
# plt.title(u'样本')
# plt.scatter(x1, x2)
# colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b']
# markers = ['o', 's', 'D', 'v', '^', 'p', '*', '+']
# tests=[2,3,4,5,8]
# subplot_counter=1
# for t in tests:
#     subplot_counter+=1
#     plt.subplot(3,2,subplot_counter)
#     kmeans_model=KMeans(n_clusters=t).fit(X)
# #     print kmeans_model.labels_:每个点对应的标签值
#     for i,l in enumerate(kmeans_model.labels_):
#         plt.plot(x1[i],x2[i],color=colors[l],
#              marker=markers[l],ls='None')
#         plt.xlim([0,10])
#         plt.ylim([0,10])
#         plt.title(u'K = %s, 轮廓系数 = %.03f' %
#                   (t, metrics.silhouette_score
#                    (X, kmeans_model.labels_,metric='euclidean')))
plt.show()
cur.close()
conn3.close()
