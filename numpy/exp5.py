# xx
#  数组复制
import numpy as np
a = np.arange(12)
b = a
print(b is a)  # true
b.shape = 3,4
print(a.shape)  #(3,4)

# def f(x):
#     print(id(x))
# print(id(a))
# print(f(a))

#浅拷贝
c = a.view()
print(c is a)   #false
print(c.base is a)  # true
print(c.flags.owndata)  #false
c.shape = 2,6
print(a.shape)
c[0,4] = 1234  #改变值
print(a)

s = a[:,1:3]  # 只在1，2 列操作
s[:] = 10
print(a)

# deep copy
d = a.copy()
print(d is a) # false
print(d.base is a)
d[0,0] = 9999
print(a)