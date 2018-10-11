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
        value = [round(x, 4) for x in df[col].values.tolist()]
        data.append({'name': col, 'x': x, 'y': value, 'active': True})
    return jsonify({'data': data})


@app.route('/data/macro/quarter/<index_name>', methods=['GET'])
def getSingleMacro(index_name):
    data = []
    td = pd.read_csv(os.path.join(Settings.tradingDay_url, 'tradingDay.csv'))
    td.index = pd.to_datetime(td['date'], format='%Y%m%d')
    td = td['20050101': datetime.datetime.now().strftime('%Y%m%d')]
    df = pd.read_excel(os.path.join(Settings.macro_url, 'macro-quarter.xlsx'))
    df = df['20050101': datetime.datetime.now().strftime('%Y%m%d')]
    td[index_name] = df[index_name]
    del td['date']
    td.fillna(method='ffill', inplace=True)
    td.fillna(method='bfill', inplace=True)
    data.append({'name': index_name, 'x': [s.strftime('%Y%m%d') for s in td.index], 'y': [round(x, 4) for x in td[index_name].tolist()]})
    return jsonify({'data': data})


@app.route('/data/macro/name', methods=['GET'])
def getMacroName():
    data = []
    df = pd.read_excel(os.path.join(Settings.macro_url, 'macro-quarter.xlsx'))
    for col in df.columns.values:
        data.append({'value': col})
    return jsonify({'data': data})


if __name__ == '__main__':
    pass