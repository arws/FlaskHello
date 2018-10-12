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
from .views import macro
from .views import pig
from .views import stock

if __name__ == '__main__':
    pass