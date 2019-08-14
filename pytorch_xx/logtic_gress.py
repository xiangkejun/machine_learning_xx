#encoding=utf-8
# 多层感知器
# 3个特征值 推出一个2分类结果

import pandas as pd
import matplotlib.pyplot as plt
# from matplotlib.font_manager import FontProperties
import tensorflow as tf

# my_font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=16)
# data = pd.read_table("F:/AI/python_xx/2fenlei.csv",sep=',')

data = pd.read_csv("2fenlei.csv",sep=',')

# data.plot.scatter(x='TV',y='sort')
# plt.show()

print(data)

x = data.iloc[:,0:-1]  # 取不要最要最后一列的数
y = data.iloc[:,-1].replace(-1,0) # 取最后一列 并将-1替换为0  变成两类 0,1

print(y)

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(4,input_shape=(3,),activation='relu'))
model.add(tf.keras.layers.Dense(4,activation='relu'))
model.add(tf.keras.layers.Dense(1,activation='sigmoid')) # 映射到 0-1 之间
# model.summary()


model.compile(optimizer='adam',
                loss='binary_crossentropy',
                metrics=['acc'])

history = model.fit(x,y,epochs=100)

# history.history.key()  # ['loss', 'acc']

plt.plot(history.epoch, history.history.get('loss'),'bo')
plt.plot(history.epoch, history.history.get('acc'),'g')
plt.show()

print(model.predict(x[:1] ))  # 取第一个做预测

