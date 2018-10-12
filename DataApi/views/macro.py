#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhangmeng
@contact: arws@qq.com
@file: macro.py
@time: 2018/10/11 14:27
"""
import datetime
import pandas as pd
import os

from flask import jsonify

from ..app import app
from ..settings import Settings


@app.route('/data/macro', methods=['GET'])
def getMacro():
    data = []

    df = pd.read_excel(os.path.join(Settings.macro_url, 'macro-quarter.xlsx'))
    x = [s.strftime('%Y%m') for s in df.index]
    for col in df.columns.values:
        value = [round(x, 6) for x in df[col].values.tolist()]
        data.append({'name': col, 'x': x, 'y': value, 'active': True})
    return jsonify({'data': data})


@app.route('/data/macro/quarter/<index_name>', methods=['GET'])
def getSingleMacro(index_name):

    d = pd.date_range(start='20050101', end=datetime.datetime.now().strftime('%Y%m%d'))

    df = pd.read_excel(os.path.join(Settings.macro_url, 'macro-quarter.xlsx'))
    df = df.reindex(d)

    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)

    return jsonify({'name': index_name, 'x': [s.strftime('%Y%m%d') for s in df.index], 'y': [round(x, 6) for x in df[index_name].tolist()]})


@app.route('/data/macro/name', methods=['GET'])
def getMacroName():
    data = []
    df = pd.read_excel(os.path.join(Settings.macro_url, 'macro-quarter.xlsx'))
    for col in df.columns.values:
        data.append({'value': col, 'label': col})
    return jsonify({'data': data})


if __name__ == '__main__':
    pass