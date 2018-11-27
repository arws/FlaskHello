#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhangmeng
@contact: arws@qq.com
@file: capitalflow.py
@time: 2018/11/5 13:15
"""
import os

import datetime
import pandas as pd

from flask import jsonify

from DataApi.Util import Const
from ...app import app
from DataApi.settings import Settings


@app.route('/data/macro/capitalflow/name', methods=['GET'])
def getCapitalFlowName():
    data = []
    df = pd.read_excel(os.path.join(Settings.data_url, 'macro', 'capitalflow.xls'))
    for col in df.columns.values:
        data.append({'value': col, 'label': col})
    return jsonify({'data': data, 'Category': '国内宏观', 'SubCategory': '资本流动'})


@app.route('/data/macro/capitalflow/single/<name>', methods=['GET'])
def getSingleCapitalFlow(name):
    d = pd.date_range(start=Const.START, end=datetime.datetime.now().strftime('%Y%m%d'))

    df = pd.read_excel(os.path.join(Settings.data_url, 'macro', 'capitalflow.xls'))
    # df.index = df['Date']
    df = df.reindex(d)

    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)

    # del df['Date']
    return jsonify({'name': name, 'x': [s.strftime('%Y%m%d') for s in df.index], 'y': [round(x, 4) for x in df[name].tolist()]})
if __name__ == '__main__':
    pass