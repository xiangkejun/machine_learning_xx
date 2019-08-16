#encoding=utf-8
# 求函数取的最小值 的 x
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt 
import torch

# (x-5)**2
def loss_f(x):
    return x**2 - 10*x + 25

x = torch.tensor([9.],requires_grad=True) # 随机初始值
optimizer = torch.optim.Adam([x],lr=1e-3)
for step in range(20000):
    pred = loss_f(x)

    optimizer.zero_grad()
    pred.backward()
    optimizer.step()

    if step % 200 == 0:
        print('step {}: x = {},f(x) = {}'
            .format(step,x.tolist(), pred.item()))