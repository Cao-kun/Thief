# -*- coding: utf-8 -*-
# @Time    : 2021/11/16 18:01
# @Author  : Caokun
# @FileName: thief_goutou.py
# @Software: PyCharm
import os

from pyquery import PyQuery
import re
import requests

# response = requests.get(url='https://mp.weixin.qq.com/s?__biz=MzkwNDE3NzgzMg==&mid=100002959&idx=1&sn=dc0e1a91764c5ee1c4046a684696481e&chksm=408bbd4877fc345ebb075b8b812058c34acf71fcaf5a92267c8ea180df991e1c4dacaf1fe163&mpshare=1&scene=1&srcid=1116PSKRxvZSyGTEAiIVS3BV&sharer_sharetime=1637056627038&sharer_shareid=00c745baa88be1cc416f931c0f781cac&key=af591244b6d224fe688719014927491c55bbf2a38154e8c2305091f9e615cedd65b151f685986ba27ed7e327400ec798193e39218689cbe4155f578679f0491aaed669ef74d877dcf12f727fab88a679066aac503312b0ccd1380fb07998f2f10e8c186879fabb7761d5d24745602aba54889bb883fb84b3373c2bac10565454&ascene=0&uin=MTQwOTAzNzEzNg%3D%3D&devicetype=Windows+10+x64&version=63040026&lang=zh_CN&exportkey=AcOyEDg69bKD6CDiyvIMSQY%3D&pass_ticket=rKf8514xU0D1iKVSGqIa61P30Yz7YQMe0UAYvRxVltW3EQHiB7pj527w8wVSvpDS&wx_header=0&fontgear=2')
# print(response.text)

doc = PyQuery('https://mp.weixin.qq.com/s?__biz=MzkwNDE3NzgzMg==&mid=100002959&idx=1&sn=dc0e1a91764c5ee1c4046a684696481e&chksm=408bbd4877fc345ebb075b8b812058c34acf71fcaf5a92267c8ea180df991e1c4dacaf1fe163&mpshare=1&scene=1&srcid=1116PSKRxvZSyGTEAiIVS3BV&sharer_sharetime=1637056627038&sharer_shareid=00c745baa88be1cc416f931c0f781cac&key=af591244b6d224fe688719014927491c55bbf2a38154e8c2305091f9e615cedd65b151f685986ba27ed7e327400ec798193e39218689cbe4155f578679f0491aaed669ef74d877dcf12f727fab88a679066aac503312b0ccd1380fb07998f2f10e8c186879fabb7761d5d24745602aba54889bb883fb84b3373c2bac10565454&ascene=0&uin=MTQwOTAzNzEzNg%3D%3D&devicetype=Windows+10+x64&version=63040026&lang=zh_CN&exportkey=AcOyEDg69bKD6CDiyvIMSQY%3D&pass_ticket=rKf8514xU0D1iKVSGqIa61P30Yz7YQMe0UAYvRxVltW3EQHiB7pj527w8wVSvpDS&wx_header=0&fontgear=2')
imgs = doc('img')

list_imgs = []
for img in imgs.items():
    if img.attr('data-src') != None:
        list_imgs.append(img.attr('data-src'))
targetDir = 'D:\AikeScrm\config_file\portrait_img'
if not os.path.isdir(targetDir):#不存在创建路径
    os.mkdir(targetDir)
num = 0
for url in list_imgs:
    print(url)
    r = requests.get(url)
    image_name = os.path.join(targetDir, str(num) + '.gif')#指定目录，图片名'xx.jpg'
    fw = open(image_name,'wb')
    fw.write(r.content)
    num +=1