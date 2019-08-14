#encoding=utf-8
# 多层感知机
# 3个特征值 推出一个连续值结果

import pandas as pd
import matplotlib.pyplot as plt
# from matplotlib.font_manager import FontProperties
import torch

# my_font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=16)
# data = pd.read_table("F:/AI/python_xx/advering.csv",sep=',')
data = pd.read_csv("advering.csv",sep=',')

# data.plot.scatter(x='TV',y='scales')
# plt.show()

print(data)

x = data.iloc[:,0:-1].as_matrix()  # 取不要最要最后一列的数
y = data.iloc[:,-1].as_matrix() # 取最后一列
print(x)

tx = torch.FloatTensor(x).reshape(-1,3)  # 3个特征
ty = torch.FloatTensor(y).reshape(-1,1)

model = torch.nn.Sequential(
    torch.nn.Linear(in_features=3, out_features=10),
    torch.nn.ReLU(),
    torch.nn.Linear(10, 1),   
    torch.nn.ReLU(),
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

    plt.scatter(t,loss.item()) 
 

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


plt.show()

print(model(tx[:1]))  # 预测地一个数据 tensor([[22.3988]], grad_fn=<ReluBackward0>)
