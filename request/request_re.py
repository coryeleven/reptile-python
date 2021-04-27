# -*- coding: utf-8 -*-
# @Time    : 2021/4/27 15:19
# @Author  : 海绵宝宝cory！！
# @FileName: request_re.py
# @Software: PyCharm
# @Description: 使用正则表达式 实现对 src 图片的聚焦抓取
import re
import  requests,os

if __name__ == '__main__':
    # url = 'https://www.qiushibaike.com/imgrank/'
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'
    # content 返回的市二进制形式的图片数据  text（字符串） content(二进制)  json(对象)
    if not os.path.exists('./tmp/qiutuLib'):
        os.makedirs('./tmp/qiutuLib')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4469.4 Safari/537.36',
    }
    for pageNum in range(1,30):
        new_url = format(url%pageNum)
    #获取整个页面的数据
        page_text= requests.get(new_url,headers).text
    #使用聚焦爬虫对页面中的所有图及逆行解析和提取
    #正则表达式
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        list_src = re.findall(ex,page_text,re.S)
        #遍历list_src,并获取图片
        for src in list_src:
            src = 'https:' + src
            img_data = requests.get(url=src,headers=headers).content
            #按/ 分割,取最后一个字段
            img_name= src.split('/')[-1]
            img_path = './tmp/qiutuLib/' + img_name
            # wb 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
            with open(img_path,'wb') as p:
                p.write(img_data)
            print(img_name,"下载成功!!!")





