#encoding=utf-8
# 多层感知器
# 3个特征值 推出一个2分类结果

import pandas as pd
import matplotlib.pyplot as plt
# from matplotlib.font_manager import FontProperties
import torch

# my_font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=16)
# data = pd.read_table("F:/AI/python_xx/2fenlei.csv",sep=',')

data = pd.read_csv("2fenlei.csv",sep=',')

# data.plot.scatter(x='TV',y='sort')
# plt.show()

print(data)

x = data.iloc[:,0:-1].as_matrix()  # 取不要最要最后一列的数
y = data.iloc[:,-1].replace(-1,0).as_matrix() # 取最后一列 并将-1替换为0  变成两类 0,1
print(y)

tx = torch.FloatTensor(x).reshape(-1,3)
ty = torch.FloatTensor(y).reshape(-1,1)


model = torch.nn.Sequential(
    torch.nn.Linear(in_features=3, out_features=4),
    torch.nn.ReLU(),
    torch.nn.Linear(4, 1),
    torch.nn.Sigmoid(),  # 二分类
)

loss_fn = torch.nn.MSELoss(reduction='sum')
learning_rate = 1e-4
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for t in range(100):
    # Forward pass: compute predicted y by passing x to the model.
    y_pred = model(tx)

    # Compute and print loss.
    loss = loss_fn(y_pred, ty)
    print(t, loss.item())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print(model(tx[:1]))  # 预测地一个数据  tensor([[1.]], grad_fn=<SigmoidBackward>)


