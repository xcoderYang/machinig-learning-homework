import kNN

import operator
import numpy as np
from matplotlib import pyplot as plt

group, labels = kNN.createDataSet()

'''
数据图
'''
# group1 = np.asarray(group)
# x = group1[..., 0]
# y = group1[..., 1]
# plt.scatter(x, y, color='r', marker='+')
# plt.show()
print(kNN.classify0([1, 1], group, labels, 3))