# -*- coding: utf-8 -*-
# @Time    : 2021/4/22 16:23
# @Author  : 海绵宝宝cory！！
# @FileName: request_html_search.py
# @Software: PyCharm
# @Description: 反爬虫策略 UA伪装：User-Agent

#UA伪装：通过修改/伪装爬虫请求的User-Agent来破解UA检测这种反爬机制
import requests
if __name__ == '__main__':
    url = 'https://www.sogou.com/web'
    #搜素数据
    word = input("Entera a word:")
    # 封装get请求参数：如果请求携带了参数，则可以将参数封装到字典中结合这requests请求方法中的data/params参数进行url参数的处理
    param = {
        'query':word,
    }
    # 自定义请求头信息:UA伪装,将包含了User-Agent的字典作用到请求方法的headers参数中即可
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4469.4 Safari/537.36',
    }
    # 发起请求
    response = requests.get(url=url, params=param, headers=headers)
    # 获取响应数据
    page_text = response.text
    print(page_text)
    filename = word + '.html'
    # 持久化存储
    with open('../tmp/'+ filename,'w',encoding='utf-8') as f:
        f.write(page_text)
    print(word,'save successful!!!')
