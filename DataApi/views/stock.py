#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhangmeng
@contact: arws@qq.com
@file: stock.py
@time: 2018/10/12 15:34
"""
import os

import datetime
import pandas as pd
from flask import jsonify

from DataApi.Util import Const
from ..Util.StockUtil import StockUtil
from ..app import app

from ..settings import Settings


@app.route('/data/stock/name', methods=['GET'])
def getStockName():
    data = []
    df = pd.read_csv(Settings.universe)
    code = df['Symbol'].map(lambda x: x[0: 6])

    for x, y in zip(code, df['ChineseName']):
        data.append({'value': x + '-' + y})
    return jsonify({'data': data})


@app.route('/data/stock/single/<code>', methods=['GET'])
def getStockData(code):
    d = pd.date_range(start=Const.START, end=datetime.datetime.now().strftime('%Y%m%d'))

    file_name = os.path.join(Settings.stock_daybar_url, code + '.csv')
    df = pd.read_csv(file_name, index_col=['Date'], usecols=['Date', 'Close'], parse_dates=True)
    df = df.reindex(d)
    try:
        divi = pd.read_csv(os.path.join(Settings.stock_dividend_url, code + '.csv'), index_col=['ExdiviDate'], usecols=['ExdiviDate', 'RatioAdjustingFactor'], parse_dates=True)
        divi = divi.reindex(d)
        df['divi'] = divi['RatioAdjustingFactor']
        df = df[Const.START: datetime.datetime.now().strftime('%Y%m%d')]
    except Exception:
        df['divi'] = 1
    df['adj_price'] = df['Close'] * df['divi']
    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)

    return jsonify({'name': StockUtil.codeToName(code), 'x': [s.strftime('%Y%m%d') for s in df.index], 'y': [round(x, 4) for x in df['adj_price'].tolist()]})


if __name__ == '__main__':
    pass