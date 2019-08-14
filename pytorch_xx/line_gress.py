#encoding=utf-8
# 拟合出一条直线

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
# from matplotlib.font_manager import FontProperties
import torch
print(torch.__version__)  # 1.2

# my_font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=16)
# data = pd.read_csv("F:/AI/python_xx/xy.csv",sep=',')

data = pd.read_csv("xy.csv",sep=',')

x = data.x
y = data.y
tx = torch.FloatTensor(x).reshape(20,1)
ty = torch.FloatTensor(y).reshape(20,1)

print(x)
print(y)
# data = [-1, -2, 1, 2]
# print(data)
# tensor = torch.FloatTensor(data)
# print(tensor)

model = torch.nn.Sequential(
    torch.nn.Linear(in_features=1, out_features=1),
    torch.nn.ReLU(),
    # torch.nn.Linear(1, 1),
)
loss_fn = torch.nn.MSELoss(reduction='sum')
learning_rate = 1e-4
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for t in range(5000):
    # Forward pass: compute predicted y by passing x to the model.
    y_pred = model(tx)

    # Compute and print loss.
    loss = loss_fn(y_pred, ty)
    print(t, loss.item())


    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


print(model(tx[:1]))  # 预测地一个数据 tensor([[0.1163]], grad_fn=<ReluBackward0>)

plt.scatter(x,y)
plt.plot(tx.numpy(),model(tx).data.numpy())
plt.show()