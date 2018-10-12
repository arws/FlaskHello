#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhangmeng
@contact: arws@qq.com
@file: StockUtil.py
@time: 2018/10/12 17:18
"""
import pandas as pd

from DataApi.settings import Settings


class StockUtil(object):

    df = pd.read_csv(Settings.universe)
    df['Code'] = df['Symbol'].map(lambda x: x[0: 6])
    df.index = df['Code']
    d = df['ChineseName'].to_dict()

    @classmethod
    def codeToName(cls, code):
        try:
            return cls.d[code]
        except KeyError:
            code


if __name__ == '__main__':
    pass