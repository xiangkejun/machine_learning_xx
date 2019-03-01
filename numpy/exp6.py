# xx
#  线性代数 linear algebra
import numpy as np
a = np.array([[1.0,2.0],[3.0,4.0]])
print(a)
print(a.transpose())  #转置
print(np.linalg.inv(a)) # 求逆

u = np.eye(2) # 单位阵
print(u)
