#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhangmeng
@contact: arws@qq.com
@file: realestate.py
@time: 2018/10/20 18:12
"""
import os

import datetime
import pandas as pd

from flask import jsonify

from ...app import app
from DataApi.settings import Settings


@app.route('/data/basic/realestate/name', methods=['GET'])
def getRealestateName():
    data = []
    df = pd.read_excel(os.path.join(Settings.data_url, 'basic', 'realestate.xls'))
    for col in df.columns.values:
        data.append({'value': col, 'label': col})
    return jsonify({'data': data, 'Category': '房地产'})


@app.route('/data/basic/realestate/single/<index_name>', methods=['GET'])
def getSingleRealestate(index_name):
    d = pd.date_range(start='20050101', end=datetime.datetime.now().strftime('%Y%m%d'))

    df = pd.read_excel(os.path.join(Settings.data_url, 'basic', 'realestate.xls'))
    # df.index = df['Date']
    df = df.reindex(d)

    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)

    # del df['Date']
    return jsonify({'name': index_name, 'x': [s.strftime('%Y%m%d') for s in df.index], 'y': [round(x, 4) for x in df[index_name].tolist()]})

if __name__ == '__main__':
    pass