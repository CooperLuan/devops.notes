# -*- coding: utf-8 -*-
"""
only works with python2

用淘宝 API 获取标准类目数据
请先填充 APP_KEY/APP_SECRET
"""
from pymongo import MongoClient
import top.api

APP_KEY = 'YOUR_APP_KEY'
APP_SECRET = 'YOU_APP_SECRET'

client = MongoClient()
db = client['taoabo']
collection = db['taobao_api_cats']

req = top.api.ItemcatsGetRequest()
req.set_app_info(top.appinfo(APP_KEY, APP_SECRET))


def get_cat(**kwargs):
    req.fields = "cid,parent_cid,name,is_parent"
    for k, v in kwargs.items():
        setattr(req, k, v)
    resp = req.getResponse()
    collection.insert(resp['itemcats_get_response']['item_cats']['item_cat'])


def main():
    if collection.count() == 0:
        get_cat(parent_cid=0)

    while 1:
        cids = [
            row['cid']
            for row in collection.find({'is_parent': True})
            if not collection.find_one({'parent_cid': row['cid']})]
        if not cids:
            break
        for cid in cids:
            print('request for cid %s' % cid)
            get_cat(parent_cid=cid)


if __name__ == '__main__':
    main()
