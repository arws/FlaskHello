#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhangmeng
@contact: arws@qq.com
@file: globalcommodity.py
@time: 2018/10/19 14:48
"""
import os

import datetime
import pandas as pd

from flask import jsonify

from DataApi.Util import Const
from DataApi.app import app
from DataApi.settings import Settings


@app.route('/data/commodity/global/name', methods=['GET'])
def getGlobalName():
    data = []
    df = pd.read_excel(os.path.join(Settings.data_url, 'basic', 'global.xls'))
    for col in df.columns.values:
        data.append({'value': col, 'label': col})
    return jsonify({'data': data, 'Category': '大宗商品', 'SubCategory': '全球大宗'})


@app.route('/data/commodity/global/single/<index_name>', methods=['GET'])
def getSingleGlobal(index_name):
    d = pd.date_range(start=Const.START, end=datetime.datetime.now().strftime('%Y%m%d'))

    df = pd.read_excel(os.path.join(Settings.data_url, 'basic', 'global.xls'))
    # df.index = df['Date']
    df = df.reindex(d)

    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)

    # del df['Date']
    return jsonify({'name': index_name, 'x': [s.strftime('%Y%m%d') for s in df.index], 'y': [round(x, 4) for x in df[index_name].tolist()]})

if __name__ == '__main__':
    pass