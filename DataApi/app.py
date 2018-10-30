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

from .views import stock

from .views.macro import consume
from .views.macro import credit
from .views.macro import gross
from .views.macro import internationaltrade
from .views.macro import investment
from .views.macro import money
from .views.macro import publicfinance

from .views.macro.america import consume
from .views.macro.america import gross
from .views.macro.america import internationaltrade
from .views.macro.america import job
from .views.macro.america import money
from .views.macro.america import realeco
from .views.macro.america import realestate

from .views.basic import allglobal
from .views.basic import domestic
from .views.basic import industryproductprice
from .views.basic import industryproductproduction
from .views.basic import industryproductproductionaccumulation
from .views.basic import realeco

from .views.FinancialMarket import bond
from .views.FinancialMarket import equity
from .views.FinancialMarket import exchange
from .views.FinancialMarket import interbank
from .views.FinancialMarket import financialmarketus
from .views.FinancialMarket import index

from .views.industry import car
from .views.industry import coal
from .views.industry import newenergymaterial
from .views.industry import pig
from .views.industry import realestate
from .views.industry import steel

from .views.industry.chem import agrichem
from .views.industry.chem import blast
from .views.industry.chem import fiber
from .views.industry.chem import mdi
from .views.industry.chem import organicraw
from .views.industry.chem import petroleum
from .views.industry.chem import plastic
from .views.industry.chem import rubber

if __name__ == '__main__':
    pass