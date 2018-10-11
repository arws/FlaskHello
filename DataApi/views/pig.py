#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhangmeng
@contact: arws@qq.com
@file: pig.py
@time: 2018/10/11 14:29
"""
import datetime
from flask import jsonify

from ..settings import Settings
from ..app import app
import pandas as pd
import os


@app.route('/data/pig', methods=['GET'])
def getPig():
    data = []

    df = pd.read_excel(os.path.join(Settings.pig_url, 'pig.xlsx'), index_col=[0])
    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)
    x = [s.strftime('%Y%m%d') for s in df.index]
    for col in df.columns.values:
        value = [round(x, 4) for x in df[col].values.tolist()]
        data.append({'name': col, 'x': x, 'y': value})
    return jsonify({'data': data})


@app.route('/data/pig/name', methods=['GET'])
def getPigName():
    data = []
    df = pd.read_excel(os.path.join(Settings.macro_url, 'pig.xls'))
    del df['Date']
    for col in df.columns.values:
        data.append({'value': col})
    return jsonify({'data': data})


@app.route('/data/pig/single/<index_name>', methods=['GET'])
def getSinglePig(index_name):
    data = []
    td = pd.read_csv(os.path.join(Settings.tradingDay_url, 'tradingDay.csv'))
    td.index = pd.to_datetime(td['date'], format='%Y%m%d')
    td = td['20050101': datetime.datetime.now().strftime('%Y%m%d')]

    df = pd.read_excel(os.path.join(Settings.pig_url, 'pig.xls'))
    df.index = pd.to_datetime(df['Date'])
    df = df['20050101': datetime.datetime.now().strftime('%Y%m%d')]

    td[index_name] = df[index_name]
    del td['date']
    td.fillna(method='ffill', inplace=True)
    td.fillna(method='bfill', inplace=True)
    data.append({'name': index_name, 'x': [s.strftime('%Y%m%d') for s in td.index], 'y': [round(x, 4) for x in td[index_name].tolist()]})
    return jsonify({'data': data})


if __name__ == '__main__':
    pass