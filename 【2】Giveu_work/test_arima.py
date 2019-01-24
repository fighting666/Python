import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller

df = pd.read_csv('E:\\Python_code\\viptest.csv', encoding='utf-8',
                 index_col='日期')
df.index = pd.to_datetime(df.index)
# print(df['进线量'])


def test_stationarity(timeseries):
    # 决定起伏统计
    rolmean = pd.rolling_mean(timeseries, window=2)    # 对size个数据进行移动平均
    rol_weighted_mean = pd.ewma(timeseries, span=2)    # 对size个数据进行加权移动平均
    rolstd = pd.rolling_std(timeseries, window=2)      # 偏离原始值多少
    # 画出起伏统计
    orig = plt.plot(timeseries, color='blue', label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    weighted_mean = plt.plot(
        rol_weighted_mean, color='green', label='weighted Mean')
    std = plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    # plt.show(block=False)
    # 进行df测试
    # print 'Result of Dickry-Fuller test'
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=[
                         'Test Statistic', 'p-value', '#Lags Used', 'Number of observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical value(%s)' % key] = value
    # print dfoutput


ts = df['进线量']
# plt.plot(ts)
# plt.show()
# test_stationarity(ts)
# plt.show()


# 估计estimating
ts_log = np.log(ts)
# plt.plot(ts_log)
# plt.show()
# moving_avg = pd.rolling_mean(ts_log, 2)
# plt.plot(moving_avg)
# plt.plot(moving_avg,color='red')
# plt.show()
# ts_log_moving_avg_diff = ts_log - moving_avg
# print ts_log_moving_avg_diff.head(12)
# ts_log_moving_avg_diff.dropna(inplace=True)
# test_stationarity(ts_log_moving_avg_diff)
# plt.show()


# 差分differencing
ts_log_diff = ts_log.diff(1)
ts_log_diff.dropna(inplace=True)
# test_stationarity(ts_log_diff)
# plt.show()


# ts_log_diff1 = ts_log.diff(1)
# ts_log_diff2 = ts_log.diff(2)
# ts_log_diff1.plot()
# ts_log_diff2.plot()
# plt.show()


# 分解decomposing
# decomposition = seasonal_decompose(ts_log)

# trend = decomposition.trend  # 趋势
# seasonal = decomposition.seasonal  # 季节性
# residual = decomposition.resid  # 剩余的

# plt.subplot(411)
# plt.plot(ts_log, label='Original')
# plt.legend(loc='best')
# plt.subplot(412)
# plt.plot(trend, label='Trend')
# plt.legend(loc='best')
# plt.subplot(413)
# plt.plot(seasonal, label='Seasonarity')
# plt.legend(loc='best')
# plt.subplot(414)
# plt.plot(residual, label='Residual')
# plt.legend(loc='best')
# plt.tight_layout()
# plt.show()

# 确定参数
# lag_acf = acf(ts_log_diff, nlags=20)
# lag_pacf = pacf(ts_log_diff, nlags=20, method='ols')
# # q的获取:ACF图中曲线第一次穿过上置信区间.这里q取2
# plt.subplot(121)
# plt.plot(lag_acf)
# plt.axhline(y=0, linestyle='--', color='gray')
# plt.axhline(y=-1.96 / np.sqrt(len(ts_log_diff)),
#             linestyle='--', color='gray')  # lowwer置信区间
# plt.axhline(y=1.96 / np.sqrt(len(ts_log_diff)),
#             linestyle='--', color='gray')  # upper置信区间
# plt.title('Autocorrelation Function')
# # p的获取:PACF图中曲线第一次穿过上置信区间.这里p取2
# plt.subplot(122)
# plt.plot(lag_pacf)
# plt.axhline(y=0, linestyle='--', color='gray')
# plt.axhline(y=-1.96 / np.sqrt(len(ts_log_diff)), linestyle='--', color='gray')
# plt.axhline(y=1.96 / np.sqrt(len(ts_log_diff)), linestyle='--', color='gray')
# plt.title('Partial Autocorrelation Function')
# plt.tight_layout()
# plt.show()


# AR model
# model = ARIMA(ts_log, order=(2, 1, 0))
# result_AR = model.fit(disp=-1)
# plt.plot(ts_log_diff)
# plt.plot(result_AR.fittedvalues, color='red')
# plt.title('AR model RSS:%.4f' % sum(result_AR.fittedvalues - ts_log_diff) ** 2)
# plt.show()

# MA model
# model = ARIMA(ts_log, order=(0, 1, 2))
# result_MA = model.fit(disp=-1)
# plt.plot(ts_log_diff)
# plt.plot(result_MA.fittedvalues, color='red')
# plt.title('MA model RSS:%.4f' % sum(result_MA.fittedvalues - ts_log_diff) ** 2)
# plt.show()


# ARIMA 将两个结合起来  效果更好
model = ARIMA(ts_log, order=(2, 1, 1))
result_ARIMA = model.fit(disp=-1)
plt.plot(ts_log_diff)
plt.plot(result_ARIMA.fittedvalues, color='red')
plt.title('ARIMA RSS:%.4f' % sum(result_ARIMA.fittedvalues - ts_log_diff) ** 2)
plt.show()

print(result_ARIMA.forecast(5)[0])

# predictions_ARIMA_diff = pd.Series(result_ARIMA.fittedvalues, copy=True)
# # print predictions_ARIMA_diff.head()#发现数据是没有第一行的,因为有1的延迟

# predictions_ARIMA_diff_cumsum = predictions_ARIMA_diff.cumsum()
# # print predictions_ARIMA_diff_cumsum.head()

# predictions_ARIMA_log = pd.Series(ts_log.ix[0], index=ts_log.index)
# predictions_ARIMA_log = predictions_ARIMA_log.add(predictions_ARIMA_diff_cumsum, fill_value=0)
# # print predictions_ARIMA_log.head()

# predictions_ARIMA = np.exp(predictions_ARIMA_log)
# plt.plot(ts)
# plt.plot(predictions_ARIMA)
# plt.title('predictions_ARIMA RMSE: %.4f' % np.sqrt(sum((predictions_ARIMA - ts) ** 2) / len(ts)))
# plt.show()



from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
from statsmodels.tsa.arima_model import ARIMA


# df = pd.read_csv('E:\\Python_code\\viptest.csv', encoding='utf-8',
#                  index_col='日期')
# print(df.head())
# print(df.head().index)
# df.index=pd.to_datetime(df.index)
# df.plot(figsize=(12,8))

# fig = plt.figure(figsize=(12,8))
# ax1= fig.add_subplot(111)
# diff1 = df.diff(1)
# diff1.plot(ax=ax1)#一阶差分

# fig = plt.figure(figsize=(12,8))
# ax2= fig.add_subplot(111)
# diff2 = df.diff(2)
# diff2.plot(ax=ax2)
# plt.show()#二阶差分

df1 = df.diff(1)  # 我们已经知道要使用一阶差分的时间序列，之前判断差分的程序可以注释掉
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(df1, lags=30, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(df1, lags=30, ax=ax2)
# plt.show()

model = ARIMA(history_price, (2, 1, 1)).fit()

model.forecast(10)[0]
