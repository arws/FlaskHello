#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhangmeng
@contact: arws@qq.com
@file: rubber.py
@time: 2018/10/26 14:20
"""
import os

import datetime
import pandas as pd

from flask import jsonify

from DataApi.app import app
from DataApi.settings import Settings


@app.route('/data/industry/chem/rubber/name', methods=['GET'])
def getRubberName():
    data = []
    df = pd.read_excel(os.path.join(Settings.data_url, 'industry/chem', 'rubber.xls'))
    for col in df.columns.values:
        data.append({'value': col, 'label': col})
    return jsonify({'data': data, 'Category': '化工', 'SubCategory': '橡胶'})


@app.route('/data/industry/chem/rubber/single/<index_name>', methods=['GET'])
def getSingleRubber(index_name):
    d = pd.date_range(start='20050101', end=datetime.datetime.now().strftime('%Y%m%d'))

    df = pd.read_excel(os.path.join(Settings.data_url, 'industry/chem', 'rubber.xls'))
    # df.index = df['Date']
    df = df.reindex(d)

    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)

    # del df['Date']
    return jsonify({'name': index_name, 'x': [s.strftime('%Y%m%d') for s in df.index], 'y': [round(x, 4) for x in df[index_name].tolist()]})


if __name__ == '__main__':
    pass