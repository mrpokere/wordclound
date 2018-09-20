# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 15:03:23 2018

@author: 2271057973
"""
import re
import requests
import time
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

pat1='"userClientShow":"(.*?)",'
pat2='"productColor":"(.*?)",'
pat3='"productSize":"(.*?)",'
        
def qingqiu(url):
    data=requests.get(url,headers=header)
    data=data.text
    time.sleep(2)
    return data
def zhenze(pat,shuju):
    x=re.compile(pat).findall(shuju)  
    time.sleep(2)
    
    return x
D=list()
for i in range(1,200):
    try:
        url1='https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv14&productId=11554626453&score=0&sortType=5&page='+str(i)+'&pageSize=10&isShadowSku=0&rid=0&fold=1'
        print('开始爬取'+str(i)+'页')
            
            
        for j in range(0,10):
                
            D.append([zhenze(pat2,qingqiu(url1))[j],zhenze(pat3,qingqiu(url1))[j],zhenze(pat1,qingqiu(url1))[j]])
    except:
        print(0)
head = ['bra颜色','bra尺寸','购买平台']


content = '\n'.join([','.join(d) for d in D])

with open('C:\\Users\\2271057973\\Desktop\\bra.small', 'w', encoding='gbk') as f:
    f.write(content.encode('gbk', 'ignore').decode('gbk'))





   


            









































