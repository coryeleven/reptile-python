# -*- coding: utf-8 -*-
# @Time    : 2021/4/23 15:58
# @Author  : 海绵宝宝cory！！
# @FileName: request_translate.py
# @Software: PyCharm
# @Description:爬取百度翻译
import json
import os

import  requests

if __name__ == '__main__':
    post_url = 'https://fanyi.baidu.com/sug'
    word = input('Enter a word:')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4469.4 Safari/537.36',
    }
    #post请求参数处理
    data = {
        'kw':word
    }
    os.mkdir('./tmp')
    # 获取响应数据:如果响应回来的数据为json，则可以直接调用响应对象的json方法获取json对象数据
    response = requests.post(url=post_url,headers=headers,data=data)

    json_data = response.json()

    filename = './tmp/'+ word + '.json'
    with open(filename,'w',encoding='utf-8') as f_json:
    #json.dump() ;两个实参，要存储的数据以及用于存储的对象文件
        json.dump(json_data,f_json,ensure_ascii=False)
    print('retpiel Over!!!')