#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhangmeng
@contact: arws@qq.com
@file: index.py.py
@time: 2018/10/11 14:28
"""
import datetime
import pandas as pd
import os

from flask import jsonify, request

from ..settings import Settings
from ..app import app
from ..Util.IndexUtil import IndexUtil


@app.route('/data/indexlist', methods=['GET', 'POST'])
def getIndexList():
    data = []
    list = [IndexUtil.nameTocode(x) for x in request.args.getlist(key='codes')]
    url = Settings.index_daybar_url
    df_dapan = pd.read_csv(os.path.join(url, '000001.csv'), index_col=['Date'], usecols=['Date', 'Close'])
    for code in list:
        file_name = os.path.join(url, code + '.csv')
        df = pd.read_csv(file_name, index_col=['Date'], usecols=['Date', 'Close'])
        df_dapan[code] = df['Close']
        df_dapan.fillna(method='ffill', inplace=True)
        df_dapan.fillna(method='bfill', inplace=True)
        data.append({'name': IndexUtil.codeToName(code), 'x': [str(s) for s in df_dapan.index.values.tolist()],
                     'y': df_dapan[code].tolist(), 'active': True})
    return jsonify({'data': data})


@app.route('/data/index/name', methods=['GET'])
def getIndexName():
    data = []
    files = os.listdir(Settings.index_daybar_url)
    names = [IndexUtil.codeToName(s[0: 6]) for s in files]
    for n in names:
        data.append({'value': n})
    return jsonify({'data': data})


@app.route('/data/index/single/<index_name>', methods=['GET'])
def getIndexData(index_name):
    d = pd.date_range(start='19890101', end=datetime.datetime.now().strftime('%Y%m%d'))

    file_name = os.path.join(Settings.index_daybar_url, IndexUtil.nameTocode(index_name) + '.csv')
    df = pd.read_csv(file_name, index_col=['Date'], usecols=['Date', 'Close'], parse_dates=True)
    df = df.reindex(d)
    df = df['20050101': datetime.datetime.now().strftime('%Y%m%d')]

    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)

    return jsonify({'name': index_name, 'x': [s.strftime('%Y%m%d') for s in df.index], 'y': [round(x, 4) for x in df['Close'].tolist()]})

if __name__ == '__main__':
    pass