# -*- coding: utf-8 -*-
# @Time    : 2021/4/28 11:14
# @Author  : 海绵宝宝cory！！
# @FileName: bs4_demo1.py
# @Software: PyCharm
# @Description:

from bs4 import  BeautifulSoup
import  lxml
import requests

if __name__ == '__main__':
     # 实例化BeautifulSoup对象
     fp = open('./tmp/index.html','r',encoding='utf-8')
     soup = BeautifulSoup(fp,'lxml')
     #返回html 中第一次出现的tagName a标签,title,script等
     print(soup.a)
     print(soup.title)
     print(soup.script)
     # find script = soup.script
     # print(soup.find('script'))


     # 获取div 中的class类
     # print(soup.find('div',class_ ='niandai_zuozhe'))
     # print(soup.find('div',class_ ='shangxi_content'))

     # 搜索html 中所有的img 标签,返回符合要求的所有标签(列表)
     print(soup.find_all('img'))
     # print(soup.select('.zz_other_shici'))
     print(soup.select('.zz_other_shici > ul > li > a ')[0]) # > 表示一个层级


