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
from .views.basic import realeco
from .views.basic import realestate

from .views.macro import consume
from .views.macro import credit
from .views.macro import gross
from .views.macro import internationaltrade
from .views.macro import investment
from .views.macro import money
from .views.macro import publicfinance

from .views.macro.america import consume
from .views.macro.america import financialmarket
from .views.macro.america import gross
from .views.macro.america import internationaltrade
from .views.macro.america import job
from .views.macro.america import money
from .views.macro.america import realeco
from .views.macro.america import realestate

from .views.FinancialMarket import bond
from .views.FinancialMarket import equity
from .views.FinancialMarket import exchange
from .views.FinancialMarket import interbank

from .views.commodity import domestic
from .views.commodity import allglobal

if __name__ == '__main__':
    pass