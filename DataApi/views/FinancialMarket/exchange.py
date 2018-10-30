#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhangmeng
@contact: arws@qq.com
@file: exchange.py
@time: 2018/10/17 15:02
"""

import os

import datetime
import pandas as pd

from flask import jsonify

from ...app import app
from DataApi.settings import Settings


@app.route('/data/financialmarket/exchange/name', methods=['GET'])
def getExchangeName():
    data = []
    df = pd.read_excel(os.path.join(Settings.data_url, 'financialMarket', 'exchange.xls'))
    for col in df.columns.values:
        data.append({'value': col, 'label': col})
    return jsonify({'data': data, 'Category': '中国金融市场', 'SubCategory': '外汇'})


@app.route('/data/financialmarket/exchange/single/<name>', methods=['GET'])
def getSingleExchange(name):
    d = pd.date_range(start='20050101', end=datetime.datetime.now().strftime('%Y%m%d'))

    df = pd.read_excel(os.path.join(Settings.data_url, 'financialMarket', 'exchange.xls'))
    # df.index = df['Date']
    df = df.reindex(d)

    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)

    # del df['Date']
    return jsonify({'name': name, 'x': [s.strftime('%Y%m%d') for s in df.index], 'y': [round(x, 4) for x in df[name].tolist()]})

if __name__ == '__main__':
    pass