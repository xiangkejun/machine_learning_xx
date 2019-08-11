# 多分类问题

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
# import tensorflow as tf


(train_image,train_label),(test_image,test_label) = tf.keras.datasets.fashion_mnist.load_data()

plt.imshow(train_image[0])

train_image = train_image / 255 
test_image = test_image /255 

print(train_image.shape)

model = tf.keras.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(units=128,activation='relu'))
model.add(tf.keras.layers.Dense(units=10, activation='softmax'))  # 多分类激活函数，将这10个类别变成概率输出

model.compile(optimizer='adam',
             #   loss='categorical_crossentropy'
                loss='sparse_categorical_crossentropy',  # 使用了数字编码类别用
                metrics=['acc'])

model.fit(train_image,train_label,epochs=5)

model.evaluate(test_image,test_label)  #