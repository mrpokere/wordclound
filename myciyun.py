# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 20:58:16 2018

@author: 2271057973
"""
import re
from wordcloud import WordCloud
from wxpy import *
import jieba
import matplotlib.pylab as plt
from PIL import Image
import numpy as np
bot=Bot()

friends=bot.friends()
bot.logout()
D = list()
for k, friend in enumerate(friends):
    signa = re.sub(r'\n', ' ', friend.signature.replace(',', '，'))
    signa = re.sub(r'<.*?>', '', signa)
    signa = re.sub(r'QQ1216753355', '', signa)
    D.append(signa)
print(D)

content='\n'.join(D)

print(content)
with open('C:\\Users\\2271057973\\Desktop\\新建文件夹\\新建文本文档.txt','w',encoding='utf-8') as f:
    f.write(content)
    f.close()
  
    
   
text=''
print('\n')
with open('C:\\Users\\2271057973\\Desktop\\新建文件夹\\新建文本文档.txt','r',encoding='utf-8') as j:
    for line in j.readlines():
            line = line.strip('\n')
    # sep’.join（seq）以sep作为分隔符，将seq所有的元素合并成一个新的字符串
            text += ' '.join(jieba.cut(line))
print(text)
a=Image.open('C:\\Users\\2271057973\\Pictures\\Saved Pictures\\太极.png')
mask=np.array(a)
wordcloud=WordCloud(font_path='./font/simhei.ttf',background_color='white',mask=mask,max_font_size=120, min_font_size=5).generate(text)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

wordcloud.to_file('C:\\Users\\2271057973\\Desktop\\77.png')































