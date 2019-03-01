#xx

#coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
#from mpl_toolkits.mplot3d import Axes3D

my_font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=16)
# fig = plt.figure()
# ax = Axes3D(fig)
# df = pd.DataFrame({'ID':[1,1,2]})
# print(df)
# df.to_excel('‪pl1.xlsx')
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

changjing_3 = pd.read_excel("F:/AI/python_xx/scene_3.xlsx")

# changjing_3.plot.scatter(x='a',y='f')

# changjing_3.plot.scatter(x='a',y='数目')

# ax1.plot(changjing_3['distance'],changjing_3['z'],'r-')
# ax2.plot(changjing_3['distance'],changjing_3['num'],'b-')

p1 = ax1.scatter(changjing_3['distance'],changjing_3['z'],c='r')
p2 = ax2.scatter(changjing_3['distance'],changjing_3['num'],c='b',marker='*')

ax1.set_xlabel("游船位置（单位:m）",fontproperties=my_font)
ax1.set_ylabel('质点坐标z值（单位:m）',fontproperties=my_font)
ax2.set_ylabel('点云数目',fontproperties=my_font)
plt.title('游船不同位置点云数目和质点坐标z值',fontproperties=my_font)
plt.legend(handles=[p1,p2,], labels=['质点坐标z值','点云数目'], loc='center right',fontsize='xx-small',prop=my_font)

plt.show()
print(changjing_3['a'])

