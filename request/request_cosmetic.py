# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 21:46
# @Author  : 海绵宝宝cory！！
# @FileName: request_cosmetic.py
# @Software: PyCharm
# @Description:

import  requests,json
if __name__ == '__main__':
    all_data = [] #存放所有企业的详细数据
    ids_list = [] #存储所有企业的ID字段

    #批量获取不同企业的ID值
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4469.4 Safari/537.36',
    }

    for page in range(1,6):
        page = str(page)
    #参数封装
        data = {
            "on": "true",
            "page": page,
            "pageSize": 15,
            "productName":"",
            "conditionType": 1,
            "applyname":"",
            "applysn":""
        }
        json_ids = requests.post(url=url,headers=headers,data=data).json()
        #遍历json 中的list列表，并取出list 列表中的ID字段
        for dic in json_ids['list']:
            #追加存入ID 到ids_list字典中
            ids_list.append(dic['ID'])

    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in ids_list:
        data_id = {
            "id":id
        }
        ids_list_info = requests.post(url=post_url,data=data_id,headers=headers).json()
        all_data.append(ids_list_info)
    fp = open('./tmp/ids_info.json','w',encoding='utf-8')
    json.dump(all_data,fp=fp,ensure_ascii=False)
    print('Over!!')