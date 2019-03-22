import keras 
import numpy as np 
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense 

x_data = np.random.rand(100)
noise = np.random.normal(0,0.01,x_data.shape)
y_data = x_data*0.1 + noise

plt.scatter(x_data,y_data)
plt.show()

model = Sequential()
model.add(Dense(units=1,input_dim=1))
model.compile(optimizer='sgd',loss='mse')

for step in range(3001):
    #每次训练一个批次
    cost = model.train_on_batch(x_data,y_data)
    if step % 500 == 0:
        print('cost:',cost)

w,b = model.layers[0].get_weights()
print('w:',w,'b:',b)

y_pred = model.predict(x_data)

plt.scatter(x_data,y_data)

plt.plot(x_data,y_pred,'r-',lw=3)
plt.show()