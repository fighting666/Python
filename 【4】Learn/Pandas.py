# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

#-------------------------------------------------------------------------------------------------------------#
# Pandas(上)学习
# 1、创建对象
# 通过一个列表的值用pandas创建一个序列
s = pd.Series([1, 3, 5, np.nan, 6, 8])  # np.nan表示不存在，缺失值
# 创建一个pandas中特有的dataframe，使用datetime作为索引和标记列名
datas = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=datas, columns=list('ABCD'))
# print df
# 使用字典来创建dataframe
df2 = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20160102'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(["test", "train", "test", "train"]),
    'F': 'foo'
})
# print df2
# print df2.dtypes  # 查看dataframe的类型信息

# 2、查看数据
df = pd.DataFrame({'total_bill': [16.99, 10.34, 23.68, 23.68, 24.59],
                   'tip': [1.01, 1.66, 3.50, 3.31, 3.61],
                   'sex': ['Female', 'Male', 'Male', 'Male', 'Female']})

print df
print df.dtypes  # 返回列数据类型
print df.shape  # 返回数据框大小
print df.head  # 返回前5行数据
print df.tail  # 返回后5行数据
print df.values  # 返回底层numpy数据
print df.index  # 返回行索引
print df.columns  # 返回列名称
print df.describe()  # 对数据的描述性统计信息，注意数据需要是数据类型(float,int)
print df.T  # 将数据框转置
print df.sort_index  # 按行索引排序
print df.sort_values(by='tip')  # 按值排序，按tip列值排序，其他数据参照B列变化

# 3、选择数据
print df['A']  # 选择一个列，返回serie,相当于df.A
# print df.A
print df[0:3]  # 通过[]切片出行数据，取出前3行数据
print df['20170102':'20170104']  # 使用新索引取出对应行

# 4、标签选择
print df.loc[datas[0]]  # 使用标签获取一块数据，取出第一行
print df.loc[:, ['A', 'B']]  # 通过标签选择多列，这里选择A\B列数据
print df.loc['20170102':'20170104', ['A', 'B']]  # 显示标签切片
print df.loc[datas[0], 'A']  # 获取标量值（定位一个具体的值）
print df.at[datas[0], 'A']  # 快速访问标量（等同于先前的方法）

# 5、按位置选择
print df.iloc[3]  # 取出下标为3的那一行
print df.iloc[3:5, 0:2]  # 通过整数切片，取出3-4行，1-2列一块区域
print df.iloc[[1, 2, 4], [0, 2]]  # 通过整数位置列表切分
print df.iloc[1:3, :]  # 切出某些行
print df.iloc[:, 1:3]  # 切出某些列
print df.iloc[1, 1]  # 获取某个值
print df.iat[1, 1]  # 同上条

# 6、布尔索引
print df[df.A > 0]  # 使用单列值选择数据，先判断A中大于0的数，然后把这些行取出来
print df[df > 0]  # 显示dataframe中大于0的数
df3 = df.copy()  # copy了一份dataframe
df3['E'] = ['one', 'one', 'two', 'three', 'four', 'three']  # 新增一列
print df3
print df3[df3['E'].isin(['two', 'four'])]  # 相当于判断two和four两列是否在E列中，返回这两列的值。

# 7、设置
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range(
    '20170101', periods=6))  # 置新的列会自动使索引对齐数据
print s1
df3['F'] = s1  # 这里用和原来一样的索引（时间）为原来的dataframe增加了一列数据
print df3
df3.loc[:, 'D'] = np.array([5] * len(df))  # 产生一个数组，每个元素值为5，长度为df的行数，替换在原来df的D列
print df3
df.iat[0, 1] = 0  # 将第一行第二列的数值设定为0
print df
df4 = df.copy()
df4[df4 > 0] = -df  # 将df copy一份命名为df4，然后将df4中大于零的数加负号
print df4

#-------------------------------------------------------------------------------------------------------------#
# Pandas(中)学习
dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print df

# 1、缺失值处理
df1 = df.reindex(index=dates[0:4], columns=list(
    df.columns) + ['E'])  # 重新索引允许您更改/添加/删除指定轴上的索引
df1.loc[dates[0]:dates[1], 'E'] = 1
print df1
print df1.dropna()  # 删除所有含有缺失值的行
print df1.dropna(how='any')  # 删除所有变量都为缺失值的行
print df1.fillna(value=5)  # 填补缺失值
print df1.fillna(method='ffill')  # 用前一个观测值填补
print df1.fillna(method='bfill')  # 用后一个观测值填补
# 用均值、中位数、方差填补
print df1.fillna('x1': x1_mean(), 'x2': x2_median, 'x3': x2_var)
print df1.fillna(0, inplace=True)
print pd.isnull(df1)  # 查看缺失值

# 2、统计
print df.mean()  # 求出每列均值
print df.mean(1)  # 求出每行均值
# APPLY
print df.apply(np.cumsum)  # 列累加，就是第二列的结果等于第一列加第二列数据，依次累加。
print df.apply(lambda x: x.max() - x.min())  # 使用匿名函数求每列的最大值和最小值的差

# 3、直方图化
s = pd.Series(np.random.randint(0, 7, size=10))
print s
print s.value_counts()  # 对数据进行计数

# 4、操作字符串的方法
# 字符串方法
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print s.str.lower()  # 把其中所有的英文字母变成小写
# 合并:字符串连接
df = pd.DataFrame(np.random.randn(10, 4))
pieces = [df[:3], df[3:7], df[7:]]
print pieces
print pd.concat(pieces)  # 用concat()将对象连接在一起
# join加入操作
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print pd.merge(left, right, on='key')  # 像笛卡尔积一样拼接
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
print pd.merge(left, right, on='key')
# append添加行
df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
print df
s = df.iloc[3]
df1 = df.append(s, ignore_index=True)  # 将第三行复制到最后一行
print df1

# 5、分组
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
print df
print df.groupby('A').sum()  # 按照A列分组并求和
# 再A列分组的基础上在B列细分，再求和
print df.groupby(['A', 'B']).sum()  # 按照多列分组形成一个分层索引，然后应用函数

# 资料重塑
# Stack堆
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))
# 创建一个list，并用zip方法整合合并成内部是tuple形式
print tuples
index = pd.MultiIndex.from_tuples(
    tuples, names=['first', 'second'])  # 将数据转化为multiindex结构，可理解为多索引结构
print index
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
print df

#-------------------------------------------------------------------------------------------------------------#

# Pandas（下）学习
# 1、数据透视表
import datetime
df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 6,
                   'B': ['A', 'B', 'C'] * 8,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 4,
                   'D': np.random.randn(24),
                   'E': np.random.randn(24),
                   'F': [datetime.datetime(2013, i, 1) for i in range(1, 13)] +
                        [datetime.datetime(2013, i, 15) for i in range(1, 13)]}
                  )
print df
print pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])

# 2、时间序列
# 创建了一个100s时间戳的系列,s为second的意思
rng = pd.date_range('2017/01/01', periods=100, freq='S')
print rng
# 产生一个时间序列为rng作为索引index,随机产生0-500之间的整数作为值
ts = pd.Series(np.random.randint(1, 500, len(rng)), index=rng)
print ts
print ts.resample('5Min').sum()  # 将该系列缩小为5分钟，没5分钟采样一次，并对其值求和：

# 3、时区表示
# 产生5个数的时间序列，偏移量为D：Day，日期
rng = pd.date_range('2017/01/01', periods=5, freq='D')
print rng
# 将产生的日期作为索引，产生日起数量（5个）的标准正态分布的数值
td = pd.Series(np.random.randn(len(rng)), rng)
print td
# 本地化时区表示：
ts_utc = ts.tz_localize('UTC')
print ts_utc
# 转换成其他时区：
ts_utc.tz_convert('US/Eastern')
print ts_utc
# 在时间跨度表示之间转换：
rng = pd.date_range('1/1/2012', periods=5, freq='M')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print ts
ps = ts.to_period()
print ps

# 4、分类
df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6], "raw_grade": [
                  'a', 'b', 'b', 'a', 'a', 'e']})
print df
# 将原始成绩转换为分类数据类型：
df["grade"] = df["raw_grade"].astype("category")
print df["grade"]
# 将类别重命名为更有意义的名称
df["grade"].cat.categories = ["very good", "good", "very bad"]
print df["grade"]
# 排序是按类别中的顺序排列的，而不是词法顺序
print df.sort_values(by="grade")

# 5、绘图
ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('2017/01/01', periods=1000))
# ts = ts.cumsum()
# tts.cumsum().plot()
# plt.show()
# plot（）可以方便地绘制带有标签的所有列,绘图必须使用show()方法才能展现出来图
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                  columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
df.plot()
plt.legend(loc='best')
plt.show()

# 6、获取数据输入\输出
df.to_csv('foo.csv')  # 写csv文件
pd.read_csv('foo.csv')  # 读取csv文件
df.to_excel('foo.xlsx', sheet_name='Sheet1')  # 写excel
pd.read_excel('foo.xlsx', 'Sheet1', index_col=None,
              na_values=['NA'])  # 读取excel文件


#-----------------------------------------------------------------------------------------------------------#

# Pandas(一)
df = pd.DataFrame({'total_bill': [16.99, 10.34, 23.68, 23.68, 24.59],
                   'tip': [1.01, 1.66, 3.50, 3.31, 3.61],
                   'sex': ['Female', 'Male', 'Male', 'Male', 'Female']})

#（1）loc，基于列label，可选取特定行（根据行index）或行标签；
#（2）iloc，基于行/列的position；
print df.loc[0]  # 通过行下标选择行数据
print df.loc[:, ['sex', 'tip']]  # 通过列标签选择多列，切片数据
print df.loc[1:3, ['sex', 'tip']]  # 通过列标签选择多列，切片数据
print df.loc[1:3, 'tip':'total_bill']  # 通过列标签选择多列，切片数据
print df.loc[0, 'sex']  # 获取标量值（定位一个具体的值）
print df.iloc[0]  # 通过行下标选择行数据
print df.iloc[1:3, [1, 2]]  # 通过行、列下标选择切片数据
print df.iloc[1:3, 1:3]  # 通过行、列下标选择切片数据
print df.iloc[[0, 2, 3], [1, 2]]  # 通过行、列下标选择切片数据
print df.iloc[0, 'sex']  # 获取标量值（定位一个具体的值）

#（1）at，根据指定行index及列label，快速定位DataFrame的元素；
#（2）iat，与at类似，不同的是根据position来定位的；
print df.at[3, 'tip']
print df.iat[3, 1]

#（1）ix，为loc与iloc的混合体，既支持label也支持position；
print df.ix[1:3, [1, 2]]
print df.ix[1:3, ['total_bill', 'tip']]

#（1）有更为简洁的行/列选取方式：
print df['tip']  # 选择一个列，返回serie
print df[1:3]  # 通过[]切片出行数据，取出前3行数据
print df[['tip', 'sex']]  # 通过[]切片出列数据，取出前2列数据

#-----------------------------------------------------------------------------------------------------------#

# Pandas读写不同文件
pd.read_sql("SQL", con=conn)
pd.read_excel('data.xlsx', 'sheet1', index=False, na_values=['NA'])
df.to_excel('data.xlsx', 'sheet1', index=False)
pd.read_csv('data.csv', 'sheet1', index=False)
df.to_csv('data.csv', 'sheet1', index=False)

# 将多张DataFrame表写入到同一个Excel的不同sheet中
# 创建一个输出文件
excelWrite = pd.ExcelWriter('out.xlsx')

data = pd.read_table('table_All_pivot.csv', sep=',')
data.to_excel(excelWrite, 'table_All_pivot', index=False)

sf_All = pd.read_table('sf_All.csv', sep=',')
sf_All.to_excel(excelWrite, 'sf_All', columns=sf_All.columns[2:], index=False)

table_All_f = pd.read_csv('table_All.csv', sep=',')
table_All_f.to_excel(excelWrite, 'table_All_f',
                     columns=table_All_f.columns[1:], index=False)

excelWrite.save()
excelWrite.close()
#-----------------------------------------------------------------------------------------------------------#
df.columns = ['a', 'b', 'c', 'd']
df.rename(columns={'$a': 'a', '$b': 'b', '$c': 'c',
                   '$d': 'd', '$e': 'e'}, inplace=True)  # 修改列名

# 数据透视表
pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True,
            margins_name='All')
# data：需要进行数据透视表操作的数据框
# values：指定需要聚合的字段
# index：指定某些原始变量作为行索引
# columns：指定哪些离散的分组变量
# aggfunc：指定相应的聚合函数
# fill_value：使用一个常数替代缺失值，默认不替换
# margins：是否进行行或列的汇总，默认不汇总
# dropna：默认所有观测为缺失的列
# margins_name：默认行汇总或列汇总的名称为'All'
