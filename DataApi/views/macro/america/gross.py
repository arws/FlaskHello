#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhangmeng
@contact: arws@qq.com
@file: gross.py
@time: 2018/10/18 14:36
"""
import os

import datetime
import pandas as pd

from flask import jsonify

from ....app import app
from DataApi.settings import Settings


@app.route('/data/macro/america/gross/name', methods=['GET'])
def getAmericaGrossName():
    data = []
    df = pd.read_excel(os.path.join(Settings.data_url, 'macro', 'america', 'gross.xls'))
    for col in df.columns.values:
        data.append({'value': col, 'label': col})
    return jsonify({'data': data, 'Category': '美国宏观', 'SubCategory': '总量'})


@app.route('/data/macro/america/gross/single/<name>', methods=['GET'])
def getSingleAmericaGross(name):
    d = pd.date_range(start='20050101', end=datetime.datetime.now().strftime('%Y%m%d'))

    df = pd.read_excel(os.path.join(Settings.data_url, 'macro', 'america', 'gross.xls'))
    df = df.loc['20050101':]
    # df.index = df['Date']
    df = df.reindex(d)

    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)

    # del df['Date']
    return jsonify({'name': name, 'x': [s.strftime('%Y%m%d') for s in df.index], 'y': [round(x, 4) for x in df[name].tolist()]})
if __name__ == '__main__':
    pass