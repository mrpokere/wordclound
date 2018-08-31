# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 18:55:08 2018

@author: 2271057973
"""

from wordcloud import WordCloud
import matplotlib.pylab as plt
import jieba
import numpy as np#为后面的图片形状做打算
from PIL import Image

f=open('C:\\Users\\2271057973\\Desktop\\新建文本文档 (2).txt').read()

text=''
with open('C:\\Users\\2271057973\\Desktop\\新建文本文档 (2).txt', 'r') as fin:
    for line in fin.readlines():
        line = line.strip('\n')
# sep’.join（seq）以sep作为分隔符，将seq所有的元素合并成一个新的字符串
        text += ' '.join(jieba.cut(line))





a=Image.open('C:\\Users\\2271057973\\Pictures\\Saved Pictures\\timg (1).jpg')

mask=np.array(a)



wordcloud=WordCloud(font_path='./font/simhei.ttf',background_color='white',mask=mask,max_font_size=100, min_font_size=30).generate(text)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

wordcloud.to_file('C:\\Users\\2271057973\\Desktop\\新建文件夹\\00.png')




























