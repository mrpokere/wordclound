# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 18:00:38 2018

@author: 2271057973
"""
import re
from os import listdir
from wordcloud import WordCloud
import jieba
from PIL import Image
import numpy as np
from matplotlib.pylab import plt
f=listdir('D:\\视频\\tim专属文件\\yellow')

#print(f)
text=''
for i in range(0,len(f)):
    
    with open('D:\\视频\\tim专属文件\\yellow\\'+f[i],encoding='ansi') as x:
        for line in x.readlines():
            line = line.strip('\n')            
            line = line.replace('<br /><br />　　','')            
            line = line.replace('<br />　　','')         
            line = line.replace('<br /><br /><br /><br /><br /><br /><br /><br />','')            
            line = line.replace('<BR>　　','')    
            line = line.replace('<br /><br />','')
            line = line.replace('<BR>','')
            line = line.replace('nbsp','')
            line = line.replace('br','')
            print(0)
            text+= ' '.join(jieba.cut(line))


a=Image.open('C:\\Users\\2271057973\\Pictures\\Saved Pictures\\太极.png')
mask=np.array(a)
wordcloud=WordCloud(font_path='./font/simhei.ttf',background_color='white',mask=mask,max_font_size=120, min_font_size=5).generate(text)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

wordcloud.to_file('C:\\Users\\2271057973\\Desktop\\2.png')
























