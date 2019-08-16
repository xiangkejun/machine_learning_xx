#encoding=utf-8
# 求函数取的最小值 的 x
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt 
import torch

# (x-5)**2
# def loss_f(x):
#     return x**2 - 10*x + 25

# 多元函数
# (x-y)**2 = 25
# x**2 +y**2-2*x*y -25 
def loss_f(x):
    return x[0]**2 + x[1]**2 -2*x[0]*x[1] - 25

x = torch.tensor([2.,1.],requires_grad=True) # 随机初始值
optimizer = torch.optim.Adam([x],lr=1e-3)
# optimizer = torch.optim.SGD([x],lr=0.01)
# optimizer = torch.optim.RMSprop([x],lr=1e-3)
for step in range(20000):
    pred = loss_f(x)

    optimizer.zero_grad()
    pred.backward()
    optimizer.step()

    if step % 200 == 0:
        print('step {}: x = {},f(x) = {}'
            .format(step,x.tolist(), pred.item()))
