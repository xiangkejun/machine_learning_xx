#encoding=utf-8
# 拟合出一条直线

import pandas as pd
import matplotlib.pyplot as plt
# from matplotlib.font_manager import FontProperties
import tensorflow as tf
print(tf.__version__)

# my_font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=16)
# data = pd.read_csv("F:/AI/python_xx/xy.csv",sep=',')

data = pd.read_csv("xy.csv",sep=',')

x = data.x
y = data.y
print(x)

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=1,input_shape=(1,)))
# model.summary() # ax+b

adam = tf.keras.optimizers.Adam(learning_rate=0.001)
print(model.predict(x))
# loss_mse = tf.keras.losses.MSE(y,model.predict(x))
model.compile(
                # optimizer='adam',
                optimizer=adam,
                loss='mse'
                # loss=loss_mse
                )

history = model.fit(x,y,
                    batch_size=2,  epochs=100)

w,b = model.layers[0].get_weights()
print('w=',w,'b=',b)  # ('w=', array([[0.2669799]], dtype=float32), 'b=', array([0.09615658], dtype=float32))

# print(model.predict(x))
print(model.predict(pd.Series([2,5])))  # 序列预测    [[0.6301164][1.4310561]]

plt.scatter(x,y)
plt.scatter(x,model.predict(x))
plt.show()
