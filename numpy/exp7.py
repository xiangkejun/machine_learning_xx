# xx
#  技巧
import numpy as np
a = np.arange(30)
a.shape = 2,-1,3  # -1自动规划形状
print(a.shape)