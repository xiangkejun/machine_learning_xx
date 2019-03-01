# xx
#  数组改变
import numpy as np
# a = np.floor(10*np.random.random((3,4)))   # return [x]
# print(a)
# print(a.ravel())  # 展平
# print(a.reshape(6,2))
# print(a.T)   #转置
# print(a.resize(2,6))  # 与reshape相同
# print(a.reshape(3,-1))  # -1 表示自适应

# 堆叠数组
# b = np.floor(10*np.random.random((2,2)))
# c = np.floor(10*np.random.random((2,2)))
# print(np.vstack((b,c)))   # 行方式堆叠
# print(np.hstack((b,c)))   # 列方式堆叠


# 1D到2D堆叠
from numpy import newaxis
# print(np.column_stack((b,c)))   #1D 到2D
# d = np.array([4.,2.])
# e = np.array([3.,8.])
# print(np.column_stack((d,e)))
# print(np.hstack((d,e)))  # 展平堆叠
# print(d[:,newaxis])
# print(np.column_stack((d[:,newaxis],e[:,newaxis])))
# print(np.hstack((d[:,newaxis],e[:,newaxis])))

# 数组拆分
f = np.floor(10*np.random.random((2,12)))
print(f)
print(np.hsplit(f,3))
print(np.hsplit(f,(3,4)))