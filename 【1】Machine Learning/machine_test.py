import numpy as np
import pandas as pd


# mysample = np.random.randint(1, 100, size=[10, 3])
mysample=np.array([[49,8,12,19,3,34,20,49,20,31],[7,19,8,37,43,17,34,14,26,41],[29,16,14,22,21,17,27,37,21,21]]).T
print(mysample)
print(np.cov(mysample.T))

dim1 = mysample[:, 0]
dim2 = mysample[:, 1]
dim3 = mysample[:, 2]

cov1 = sum((dim1 - np.mean(dim1)) * (dim2 - np.mean(dim2)))/(np.size(mysample[:, 1]) - 1)
cov2 = sum((dim1 - np.mean(dim1)) * (dim3 - np.mean(dim3)))/(np.size(mysample[:, 1]) - 1)
cov3 = sum((dim2 - np.mean(dim2)) * (dim3 - np.mean(dim3)))/(np.size(mysample[:, 1]) - 1)
print(cov1,cov2,cov3)

var1 = np.var(dim1)
var2 = np.var(dim2)
var3 = np.var(dim3) 
print(var1,var2,var3)




 