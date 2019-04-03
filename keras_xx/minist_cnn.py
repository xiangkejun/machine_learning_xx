
import numpy as np 
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout,Convolution2D,MaxPooling2D,Flatten
from keras.optimizers import Adam

(x_train,y_train),(x_test,y_test) = mnist.load_data()
# (6000,28,28) --> (6000,28,28,1)
x_train = x_train.reshape(-1,28,28,1)/255.0
x_test = x_test.reshape(-1,28,28,1)/255.0
# 换 one-hot 格式
y_train = np_utils.to_categorical(y_train,num_classes=10)
y_test = np_utils.to_categorical(y_test,num_classes=10)

model = Sequential()
model.add(Convolution2D(
    input_shape = (28,28,1),
    filters = 32,
    kernel_size = 5,
    strides = 1,
    padding ='same',
    activation = 'relu'
))

model.add(MaxPooling2D(
    pool_size=2,
    strides=2,
    padding='same'
))

model.add(Convolution2D(64,5,strides=1,padding='same',activation='relu'))
model.add(MaxPooling2D(2,2,'same'))

model.add(Flatten())

model.add(Dense(1024,activation = 'relu'))
model.add(Dropout(0.5))

model.add(Dense(10,activation='softmax'))

#定义优化器
adam = Adam(lr = 1e-4) # 0.0001
model.compile(optimizer=adam,loss='categorical_crossentropy',metrics=['accuracy'])

model.fit(x_train,y_train,batch_size=64,epochs=10)

loss,accuracy = model.evaluate(x_test,y_test)

print('test loss:',loss)
print('test accuracy:',accuracy)