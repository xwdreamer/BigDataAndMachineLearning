

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN



data = pd.read_csv('country_data.csv')

# 读取前五行数据，如果是最后五行，用data.tail()
print(data.head(5))

# 我们看看数据的维度：
print(data.shape)


# 现在我们开始准备样本特征X，我们用AT， V，AP和RH这4个列作为样本特征。
X = data[['面积km2', '人口']]
print(X.head())

#转换 成 numpy array, 这个数据没有head
X=np.array(X)


#做归一化，a是面积，b是人口
a = X[:, :1] / 17075400.0 * 10000
b = X[:, 1:] / 1392358258.0 * 10000
X = np.concatenate((a,b), axis=1)

print(a)
print('#############################')
print(b)
