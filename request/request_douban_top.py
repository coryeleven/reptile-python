# -*- coding: utf-8 -*-
# @Time    : 2021/4/23 17:03
# @Author  : 海绵宝宝cory！！
# @FileName: request_douban.top.py
# @Software: PyCharm
# @Description: 豆瓣高分电影
import requests,json

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list?'
    param = {
        'type':'24',
        'interval_id':'100:90',
        'action':'',
        'start': 0,
        'limit': 20,
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4469.4 Safari/537.36',
    }
    response = requests.get(url=url,params=param,headers=headers)
    #调用response 的json 方法
    list_data = response.json()

    with open('../tmp/douban.json','w',encoding='utf-8') as f_douban:
        json.dump(list_data,f_douban,ensure_ascii=False)
    print("Movie save Over!!!")