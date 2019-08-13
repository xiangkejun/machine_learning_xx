#encoding=utf-8
# 多分类问题
# 手动保存 *.h5 权重

from __future__ import absolute_import, division, print_function, unicode_literals

import os
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow import keras

print(tf.version.VERSION)

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

train_labels = train_labels[:1000]
test_labels = test_labels[:1000]

plt.imshow(train_images[0])  # 5
plt.show()

train_images = train_images[:1000].reshape(-1, 28 * 28) / 255.0
test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0

# 定义一个简单的序列模型
def create_model():
    model = tf.keras.models.Sequential([
      keras.layers.Dense(512, activation='relu', input_shape=(784,)),
      keras.layers.Dropout(0.2),
      keras.layers.Dense(10, activation='softmax')
    ])
  
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
  
    return model
  
  # 创建一个基本的模型实例
model = create_model()
  
# 显示模型的结构
model.summary()

# 使用新的回调训练模型
model.fit(train_images, 
          train_labels,  
          epochs=5,
          )  

# 保存权重
model.save('my_model.h5')

# Evaluate the model
loss,acc = model.evaluate(test_images, test_labels)
print(" model, accuracy: {:5.2f}%".format(100*acc))

print(model.predict(train_images[:1])) # [[2.5317803e-04 7.2924799e-04 1.4610562e-03 7.4771196e-02 9.9087765e-06
  # 9.1992557e-01 2.5099045e-05 9.3348324e-04 1.7478490e-03 1.4335765e-04]]
