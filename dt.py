# -*- coding: utf-8 -*-

"""
Create at 16/10/28
"""

__author__ = 'TT'
import time


def format_datetime(st):
    """"""
    return int(time.mktime(time.strptime(st, "%Y-%m-%d %H:%M:%S")))


st = '2016-12-01 00:00:00'

print format_datetime(st)
