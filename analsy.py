# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 22:15:43 2018

@author: 2271057973
"""

import pandas as pda
import numpy as npy
import matplotlib.pyplot as plt
from collections import Counter

data=pda.read_csv('C:\\Users\\2271057973\\Desktop\\brasmall.csv',encoding='gbk')
data=data.T
bracolor=data.values[0]
brasize=data.values[1]
brastage=data.values[2]

c1=Counter(bracolor)
c2=Counter(brasize)
c3=Counter(brastage)


print(c1)
print()
print(c2)
print()
print(c3)
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
'''
#小号A-C
labels=[u'紫色',u'肤色',u'黑色',u'浅紫色',u'银灰色',u'虾红色',u'红色']
sizes=[814,844,366,261,212,119,278]
colors=['purple','gold','brown','blue','gray','orange','red']
explode=[0,0,0,0,0,0,0]
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)

plt.axis('equal')
plt.show()

labels=['75B','80B','75A','80A','85B','70A','70B','90C','85C','80C','85A','75C','70C']
sizes=[1202,331,311,258,186,122,113,112,101,78,77,73,6]
colors=['purple','gold','darkgray','blue','gray','orange','red','aliceblue','aqua','blanchedalmond','brown','cyan','darkgoldenrod']
explode=[0,0,0,0,0,0,0,0,0,0,0,0,0]
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)

plt.axis('equal')
plt.show()

labels=[u'来自京东Android客户端',u'来自京东iPhone客户端',u'来自京东iPad客户端',u'来自微信购物',u'来自手机QQ购物']
sizes=[2103,533,2,256,6]
colors=['purple','gold','brown','blue','gray']
explode=[0,0,0,0,0]
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)

plt.axis('equal')
plt.show()
'''
#大号B以上
labels=[u'宝蓝色',u'粉色',u'黑色',u'白色',u'藕荷色',u'蓝绿色',u'烟紫',u'大红',u'蓝绿']
sizes=[844,635,745,147,812,104,127,76,37]
colors=['blue','pink','brown','white','lightpink','blue','purple','red','green']
explode=[0,0,0,0,0,0,0,0,0]
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)

plt.axis('equal')
plt.show()
'''
'宝蓝色': 844
'粉色': 400
黑色': 745
白色': 147
藕荷色': 812
'粉色': 235
'蓝绿色': 104
'烟紫':127
'大红': 76
'蓝绿': 37
'''
labels=['80C','85B','85C','80B','75B','75E','75C','80E','85E','85D','90B','90E','90C','80D','75D','80F','70E','90D']
sizes=[1449,166,277,322,241,23,258,28,26,97,3,5,11,116,  63, 3,12,7]
colors=['blue','pink','brown','white','lightpink','blue','purple','red','green','lightyellow','midnightblue','mistyrose','oldlace','olive'
,'olivedrab'
,'orange'
,'orangered']
explode=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)

plt.axis('equal')
plt.show()
'''
'80C': 1449,  '85B':166, '85C': 277, '80B': 322, '75B': 241, '75E': 23, '75C': 38+ 230, '80E':28,
 '85E': 26,
 '85D': 97, '90B': 3, '90E': 5, '90C': 11, '80D':116, '75D': 63，'80F': 3，'70E': 12，90D': 7，'75F': 5

'''
labels=[u'来自京东Android客户端',u'来自京东iPhone客户端',u'来自京东iPad客户端',u'来自微信购物',u'来自手机QQ购物']
sizes=[793,1327,6,130,7]
colors=['purple','gold','brown','blue','gray']
explode=[0,0,0,0,0]
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)

plt.axis('equal')
plt.show()
'''
来自京东Android客户端': 2103+40, '来自京东iPhone客户端': 533+665,
 '来自微信购物': 262, nan: 70, '来自手机QQ购物': 6, '来自京东iPad客户端': 2
'''





