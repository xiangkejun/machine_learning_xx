# xx
#  技巧
import numpy as np

a = np.arange(30)
a.shape = 2,-1,3  # -1自动规划形状
print(a.shape)

# 矢量堆叠
x = np.arange(0,10,2)
y = np.arange(5)
print(np.vstack([x,y]))
print(np.hstack([x,y]))