# -*- coding: utf-8 -*-

"""
Create at 16/10/20
"""

__author__ = 'TT'

import sqlite3
import struct


conn = sqlite3.connect('161114/Manifest.db')

res = conn.execute("select * FROM Files WHERE relativePath like '%MM%sqlite%' and domain like '%xin%' ")
for i in res.fetchall():
    print i
    file_info = open(i[-1]).read()

    print file_info
