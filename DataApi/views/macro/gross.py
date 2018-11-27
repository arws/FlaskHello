#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhangmeng
@contact: arws@qq.com
@file: gross.py
@time: 2018/10/17 15:41
"""
import os

import datetime
import pandas as pd

from flask import jsonify

from DataApi.Util import Const
from ...app import app
from DataApi.settings import Settings


@app.route('/data/macro/gross/name', methods=['GET'])
def getGrossName():
    data = []
    df = pd.read_excel(os.path.join(Settings.data_url, 'macro', 'gross.xls'))
    for col in df.columns.values:
        data.append({'value': col, 'label': col})
    return jsonify({'data': data, 'Category': '国内宏观', 'SubCategory': '总量'})


@app.route('/data/macro/gross/single/<name>', methods=['GET'])
def getSingleGross(name):
    d = pd.date_range(start=Const.START, end=datetime.datetime.now().strftime('%Y%m%d'))

    df = pd.read_excel(os.path.join(Settings.data_url, 'macro', 'gross.xls'))
    # df.index = df['Date']
    df = df.reindex(d)

    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)

    # del df['Date']
    return jsonify({'name': name, 'x': [s.strftime('%Y%m%d') for s in df.index], 'y': [round(x, 4) for x in df[name].tolist()]})
if __name__ == '__main__':
    pass