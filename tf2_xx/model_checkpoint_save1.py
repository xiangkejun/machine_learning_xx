# https://tensorflow.google.cn/tutorials/keras/save_and_restore_models
## 在训练期间保存模型
# 在回调函数中实现（以 checkpoints 形式保存)

from __future__ import absolute_import, division, print_function, unicode_literals

import os

import tensorflow as tf
from tensorflow import keras

print(tf.version.VERSION)

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

train_labels = train_labels[:1000]
test_labels = test_labels[:1000]

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

###### 在训练期间保存模型（以 checkpoints 形式保存）
checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# 创建一个保存模型权重的回调
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)

# 使用新的回调训练模型
model.fit(train_images, 
          train_labels,  
          epochs=10,
          validation_data=(test_images,test_labels),
          callbacks=[cp_callback])  # 通过回调训练

# 这可能会生成与保存优化程序状态相关的警告。
# 这些警告（以及整个笔记本中的类似警告）是防止过时使用，可以忽略。
