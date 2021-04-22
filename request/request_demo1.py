# -*- coding: utf-8 -*-
# @Time    : 2021/4/22 15:29
# @Author  : 海绵宝宝cory！！
# @FileName: request_demo1.py
# @Software: PyCharm
# @Description:

import requests,os

if __name__ == '__main__':
    url = 'https://www.sogou.com/'
    response = requests.get(url=url)
    page_text = response.text
    print(page_text)
    # os.mkdir('./tmp')
    with open('../tmp/sougou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print("爬取数据结束")


