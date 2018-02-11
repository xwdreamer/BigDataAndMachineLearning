# http://dataconomy.com/2015/02/linear-regression-implementation-in-python/
# https://www.cnblogs.com/hhh5460/p/5786115.html

# Required Packages
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model

# Function to get data
# read  房屋面积与价格历史数据(csv文件)
data = pd.read_csv('input_data.csv')

#输出 csv文件内容
print(data.head(10))
print(data.shape)

#拆分csv数组
X = data['Square_Feet']
Y = data['Price']

#输出X\Y
print(X.head(5))
print(Y.head(5))

# 建立线性回归模型

linreg = linear_model.LinearRegression()
# 以下函数被废弃，使用.values.reshape()
#linreg.fit(X.reshape(-1, 1),Y)
linreg.fit(X.values.reshape(-1, 1),Y)

# 输出一次方程参数
print (linreg.intercept_)
print (linreg.coef_)

# 根据现行回归求Y值
Y_pred = linreg.predict(X.values.reshape(-1, 1))

# 输出训练集散点
plt.scatter(X, Y,  color='black')

# 输出回归曲线
plt.plot(X, Y_pred, color='blue', linewidth=3)
#是否显示坐标
#plt.xticks(())
#plt.yticks(())

plt.show()






