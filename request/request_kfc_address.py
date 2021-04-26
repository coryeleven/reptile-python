# -*- coding: utf-8 -*-
# @Time    : 2021/4/23 17:03
# @Author  : 海绵宝宝cory！！
# @FileName: request_douban.top.py
# @Software: PyCharm
# @Description: kfc 地址爬取
import requests,json

if __name__ == '__main__':
    address_name = input("Enter a address:")
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    data = {
        'cname':'',
        'pid':'',
        'keyword': address_name,
        'pageIndex': '1',
        'pageSize': '10',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4469.4 Safari/537.36',
    }
    response = requests.post(url=url,data=data,headers=headers)
    #调用response 的json 方法
    list_data = response.json()

    with open('../tmp/'+address_name+'.json','w',encoding='utf-8') as f_kfc:
        json.dump(list_data,f_kfc,ensure_ascii=False)
    print("Movie save Over!!!")