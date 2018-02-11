

#http://www.cnblogs.com/pinard/p/6016029.html

import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
import pandas as pd

# read_csv里面的参数是csv在你电脑上的路径，此处csv文件放在notebook运行目录下面的CCPP目录里
data = pd.read_csv('ccpp1.csv')


#读取前五行数据，如果是最后五行，用data.tail()
print(data.head(5))

# 我们看看数据的维度：
print(data.shape)

# 现在我们开始准备样本特征X，我们用AT， V，AP和RH这4个列作为样本特征。
X = data[['AT', 'V', 'AP', 'RH']]
print(X.head())


#　接着我们准备样本输出y， 我们用PE作为样本输出。

y = data[['PE']]
print(y.head())



# from sklearn.cross_validation import train_test_split  ,  此函数已经被弃用，使用下面的函数
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)


print (X_train.shape)
print (y_train.shape)
print (X_test.shape)
print (y_test.shape)




from sklearn.linear_model import LinearRegression
linreg = LinearRegression() # 建立线性回归模型
linreg.fit(X_train, y_train)


print (linreg.intercept_)
print (linreg.coef_)



#模型拟合测试集
y_pred = linreg.predict(X_test)
from sklearn import metrics
# 用scikit-learn计算MSE
print ("MSE:",metrics.mean_squared_error(y_test, y_pred))
# 用scikit-learn计算RMSE
print ("RMSE:",np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


X = data[['AT', 'V', 'AP', 'RH']]
y = data[['PE']]
from sklearn.model_selection import cross_val_predict
predicted = cross_val_predict(linreg, X, y, cv=10)
# 用scikit-learn计算MSE
print("MSE:",metrics.mean_squared_error(y, predicted))
# 用scikit-learn计算RMSE
print("RMSE:",np.sqrt(metrics.mean_squared_error(y, predicted)))


fig, ax = plt.subplots()
ax.scatter(y, predicted)
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()

