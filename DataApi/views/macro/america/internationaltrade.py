#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhangmeng
@contact: arws@qq.com
@file: internationaltrade.py
@time: 2018/10/18 14:37
"""
import os

import datetime
import pandas as pd

from flask import jsonify

from DataApi.Util import Const
from ....app import app
from DataApi.settings import Settings


@app.route('/data/macro/america/internationaltrade/name', methods=['GET'])
def getAmericaInternationaltradeName():
    data = []
    df = pd.read_excel(os.path.join(Settings.data_url, 'macro', 'america', 'internationaltrade.xls'))
    for col in df.columns.values:
        data.append({'value': col, 'label': col})
    return jsonify({'data': data, 'Category': '美国宏观', 'SubCategory': '国际贸易'})


@app.route('/data/macro/america/internationaltrade/single/<name>', methods=['GET'])
def getSingleAmericaInternationaltrade(name):
    d = pd.date_range(start=Const.START, end=datetime.datetime.now().strftime('%Y%m%d'))

    df = pd.read_excel(os.path.join(Settings.data_url, 'macro', 'america', 'internationaltrade.xls'))
    df = df.loc[Const.START:]
    # df.index = df['Date']
    df = df.reindex(d)

    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)

    # del df['Date']
    return jsonify({'name': name, 'x': [s.strftime('%Y%m%d') for s in df.index], 'y': [round(x, 4) for x in df[name].tolist()]})
if __name__ == '__main__':
    pass