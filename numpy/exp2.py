# xx
# 基本操作
import numpy as np
# a = np.array([20,30,40,50])
# b = np.arange(4)
# print(a - b)
# print(b**2)
# print(10*np.sin(a))
# print(a < 35)

# A = np.array([[1,1],
#             [0,1]])
# B = np.array([[2,0],
#             [3,4]])
# print(A*B)  # 元素与元素相乘
# print(A@B)  # 矩阵相乘
# print(A.dot(B))

# c = np.random.random((2,3))
# print(c)
# print(c.sum())
# print(c.min())
# print(c.max())

# d = np.arange(12).reshape(3,4)
# print(d)
# print(d.sum(axis = 0))
# print(d.min(axis = 1))
# print(d.cumsum(axis = 1))


C = np.arange(3)
print(np.exp(C))
print(np.sqrt(C))
D = np.array([2,-1,4])
print(np.add(C,D))