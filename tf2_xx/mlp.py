# 多层感知器
# 3个特征值 推出一个结果

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
# import tensorflow as tf

my_font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=16)
data = pd.read_table("F:/AI/python_xx/advering.csv",sep=',')

data.plot.scatter(x='TV',y='scales')

plt.show()

print(data)

x = data.iloc[:,0:-1]  # 取不要最要最后一列的数
y = data.iloc[:,-1] # 取最后一列

print(x)

model = tf.keras.Sequential([tf.keras.layers.Dense(10,input_shape=(3,),activation='relu'),  #第一层
                            tf.keras.layers.Dense(1)]  # 第二层
                            )
model.compile(optimizer='adam',
                loss='mse')

model.fit(x,y,epochs=100)

test = data.iloc[:1,0:-1] #取前两个数据做预测
model.predict(test)

