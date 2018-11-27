#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhangmeng
@contact: arws@qq.com
@file: buildmaterial.py
@time: 2018/10/31 14:49
"""
import os

import datetime
import pandas as pd

from flask import jsonify

from DataApi.Util import Const
from DataApi.app import app
from DataApi.settings import Settings


@app.route('/data/industry/buildmaterial/name', methods=['GET'])
def getBuildMaterialName():
    data = []
    df = pd.read_excel(os.path.join(Settings.data_url, 'industry', 'buildmaterial.xls'))
    for col in df.columns.values:
        data.append({'value': col, 'label': col})
    return jsonify({'data': data, 'Category': '建材'})


@app.route('/data/industry/buildmaterial/single/<index_name>', methods=['GET'])
def getSingleBuildMaterial(index_name):
    d = pd.date_range(start=Const.START, end=datetime.datetime.now().strftime('%Y%m%d'))

    df = pd.read_excel(os.path.join(Settings.data_url, 'industry', 'buildmaterial.xls'))
    # df.index = df['Date']
    df = df.reindex(d)

    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)

    # del df['Date']
    return jsonify({'name': index_name, 'x': [s.strftime('%Y%m%d') for s in df.index], 'y': [round(x, 4) for x in df[index_name].tolist()]})
if __name__ == '__main__':
    pass