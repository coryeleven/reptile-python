# -*- coding: utf-8 -*-
# @Time    : 2021/4/27 15:46
# @Author  : 海绵宝宝cory！！
# @FileName: Regular_demo1.py
# @Software: PyCharm
# @Description:

import  re

print(re.match('www','www.baidu.com').span())
print(re.match('com','www.baidu.com'))

line = 'Cats are smarter than logs'
matchObj = re.match(r'(.*)are(.*?).*',line,re.M|re.I)

if matchObj:
    print('matchObj.group():',matchObj.group())
    print('matchObj.group(1):',matchObj.group(1))
    print('matchObj.group(2):',matchObj.group(2))
else:
    print('No match!!')

#提取出python
key="javapythonc++php"
print(re.findall('python',key)[0])