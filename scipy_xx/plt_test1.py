
# https://www.jianshu.com/p/5392170c5fee
# plt.ion()  和 plt.ioff()

#encoding=utf-8

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__' :
    t1 = np.arange(0, 30, 0.1)
    plt.figure()
    plt.ion()
    for i in range(100):
        plt.ylim(-10, 10) #此处限制了一下y轴坐标最大最小值，防止刻度变化，不利于观察。
        plt.plot(t1, 0.1*i*np.sin(t1 + 0.1 * i))
        plt.plot(t1, 0.1 * (i -100) * np.cos(t1 + 0.2 * i))
        plt.pause(0.01)
        plt.clf()
    plt.ioff()