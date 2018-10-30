#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhangmeng
@contact: arws@qq.com
@file: index.py
@time: 2018/10/30 13:42
"""
import datetime
import pandas as pd
import os

from flask import jsonify, request

from DataApi.settings import Settings
from DataApi.app import app


@app.route('/data/financialmarket/index/indexlist', methods=['GET', 'POST'])
def getIndexList():
    data = []
    d = pd.date_range(start='20050101', end=datetime.datetime.now().strftime('%Y%m%d'))
    list = request.args.getlist(key='codes')
    df = pd.read_excel(os.path.join(Settings.data_url, 'financialMarket', 'index.xls'))
    df = df.reindex(d)

    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)

    for col in list:
        data.append({'name': col, 'x': [s.strftime('%Y%m%d') for s in df.index], 'y': [round(x, 4) for x in df[col].tolist()]})

    return jsonify({'data': data})


@app.route('/data/financialmarket/index/name', methods=['GET'])
def getIndexName():
    data = []
    df = pd.read_excel(os.path.join(Settings.data_url, 'financialMarket', 'index.xls'))
    for col in df.columns.values:
        data.append({'value': col})
    return jsonify({'data': data})


@app.route('/data/financialmarket/index/single/<index_name>', methods=['GET'])
def getIndexData(index_name):
    d = pd.date_range(start='20050101', end=datetime.datetime.now().strftime('%Y%m%d'))

    df = pd.read_excel(os.path.join(Settings.data_url, 'financialMarket', 'index.xls'))
    df = df.reindex(d)

    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)

    # del df['Date']
    return jsonify({'name': index_name, 'x': [s.strftime('%Y%m%d') for s in df.index], 'y': [round(x, 4) for x in df[index_name].tolist()]})


if __name__ == '__main__':
    pass