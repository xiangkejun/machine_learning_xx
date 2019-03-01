# xx
#  线性代数 linear algebra
import numpy as np
a = np.array([[1.0,2.0],[3.0,4.0]])
print(a)
print(a.transpose())  #转置
print(np.linalg.inv(a)) # 求逆

u = np.eye(2) # 单位阵
print(u)
print(np.trace(u)) #对角线的和 2.0
j = np.array([[0.0,-1.0],[1.0,0.0]])
y = np.array([[5.],[7.]])
print(np.linalg.solve(a,y)) # 求ax=y的解
print(np.linalg.eig(j)) # 求特征值和特征向量
