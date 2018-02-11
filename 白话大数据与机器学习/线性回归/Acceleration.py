# 房价预测案例
# 白话机器学习8.2章节示例

# Required Packages
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model

# Function to get data
# 读取重力加速度训练值
data = pd.read_csv('Acceleration_data2.csv')

#输出 csv文件内容
print(data.head(10))
print(data.shape)

#拆分csv数组
X = data['t']
Y = data['v']

#输出X\Y
print(X.head(5))
print(Y.head(5))

# 建立线性回归模型

linreg = linear_model.LinearRegression()
# 以下函数被废弃，使用.values.reshape()
#linreg.fit(X.reshape(-1, 1),Y), 表示一维数组
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






