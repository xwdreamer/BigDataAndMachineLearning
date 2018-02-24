
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_csv('sh_area_level2.csv')
# data = pd.read_csv('sh_area_level3.csv')

# 读取前五行数据，如果是最后五行，用data.tail()
print(data.head(5))

# 我们看看数据的维度：
print(data.shape)

# 现在我们开始准备样本特征X，我们用AT， V，AP和RH这4个列作为样本特征。
X = data[['lng', 'lat']]
print(X.head())

# #############################################################################
# Compute clustering with Means

#转换 成 numpy array ，不转换会报错
X=np.array(X)
#print(X.head())

n_clusters = 5

k_means = KMeans(n_clusters)
t0 = time.time()
cls = k_means.fit(X)
t_batch = time.time() - t0

cls.labels_

# 画图
markers = ['^', 'x', 'o', '*', '+']
for i in range(n_clusters):
    members = cls.labels_ == i
    plt.scatter( X[members,0], X[members,1], s=60, marker=markers[i], c='b', alpha= 0.5)



print(t_batch)
print(k_means.inertia_)
plt.title('K-Means')
plt.show()


