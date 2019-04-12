#xx

#coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

my_font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=16)
pose = pd.read_table("F:/AI/python_xx/xy.txt",sep=',')
pose.plot.scatter(x='x',y='y')

plt.show()
