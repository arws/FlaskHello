#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhangmeng
@contact: arws@qq.com
@file: equity.py
@time: 2018/10/17 15:02
"""
import os

import datetime
import pandas as pd

from flask import jsonify

from DataApi.Util import Const
from ...app import app
from DataApi.settings import Settings


@app.route('/data/financialmarket/equity/name', methods=['GET'])
def getEquityName():
    data = []
    df = pd.read_excel(os.path.join(Settings.data_url, 'financialmarket', 'equity.xls'))
    for col in df.columns.values:
        data.append({'value': col, 'label': col})
    return jsonify({'data': data, 'Category': '中国金融市场', 'SubCategory': '权益'})


@app.route('/data/financialmarket/equity/single/<name>', methods=['GET'])
def getSingleEquity(name):
    d = pd.date_range(start=Const.START, end=datetime.datetime.now().strftime('%Y%m%d'))

    df = pd.read_excel(os.path.join(Settings.data_url, 'financialmarket', 'equity.xls'))
    # df.index = df['Date']
    df = df.reindex(d)

    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)

    # del df['Date']
    return jsonify({'name': name, 'x': [s.strftime('%Y%m%d') for s in df.index], 'y': [round(x, 4) for x in df[name].tolist()]})
if __name__ == '__main__':
    pass