
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN

data = pd.read_csv('province_data.csv')

# 读取前五行数据，如果是最后五行，用data.tail()
print(data.head(5))

# 我们看看数据的维度：
print(data.shape)


# 现在我们开始准备样本特征X，我们用AT， V，AP和RH这4个列作为样本特征。
X = data[['population', 'area2']]
print(X.head())

# #############################################################################
# Compute clustering with Means

#转换 成 numpy array ，不转换会报错
X=np.array(X)
#print(X.head())

#做归一化，a是人口，b是面积，面积单位平方千米
a = X[:, :1] / 104303132.0 * 10000
b = X[:, 1:] / 1660000.0 * 10000
X = np.concatenate((a,b), axis=1)

# #############################################################################
# Compute DBSCAN
db = DBSCAN(eps=2000, min_samples=1).fit(X)
labels = db.labels_

print(labels)

# Number of clusters in labels, ignoring noise if present.
n_clusters = len(set(labels))


# 画图
markers = ['^', 'x', 'o', '*', '+']
for i in range(n_clusters):
    members = labels == i
    plt.scatter( X[members,0], X[members,1], s=60, marker=markers[i], c='b', alpha= 0.5)


plt.title('DBSCAN')
plt.show()


