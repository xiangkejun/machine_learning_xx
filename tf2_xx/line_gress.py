import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
# import tensorflow as tf

my_font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=16)
data = pd.read_table("F:/AI/python_xx/xy.csv",sep=',')

# data.plot.scatter(x='x',y='y')

# plt.show()

x = data.x
y = data.y
print(x)

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1,input_shape=(1,)))
# model.summary() # ax+b

model.compile(optimizer='adam',
                loss='mse')

history = model.fit(x,y,epochs=100)

model.predit(x)
model.predit(pd.Series([2,5]))  # 序列预测