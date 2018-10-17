#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhangmeng
@contact: arws@qq.com
@file: app.py
@time: 2018/10/11 14:28
"""
from flask import Flask

app = Flask(__name__)

from .views import index

from .views import stock

from .views.basic import pig

from .views.macro import consume
from .views.macro import credit
from .views.macro import gross
from .views.macro import internationaltrade
from .views.macro import investment
from .views.macro import money
from .views.macro import publicfinance

from .views.FinancialMarket import bond
from .views.FinancialMarket import equity
from .views.FinancialMarket import exchange
from .views.FinancialMarket import interbank

if __name__ == '__main__':
    pass