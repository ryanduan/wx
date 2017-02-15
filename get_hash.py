# -*- coding: utf-8 -*-

"""
Create at 16/10/20
"""

__author__ = 'TT'

import hashlib


# s = 'wangwangxuebing564'
# s = 'linlin748060'
s = 'drazengy'
md5 = hashlib.md5()

ed = '/MM.sqlite'

s1 = '2725175731508b12f76188d3c617c78432a9dfcb'
s2 = '4c30ba2512102a58ab13584b2e170b42'
md5.update(s)

# print len('23f4a474440e98d551e2e686f6a948f4ae28afc3')

res = md5.hexdigest()
print res
print len('dee67bd47fc19a4633014044b3058d5f')

print len('5f4dcc3b5aa765d61d8327deb882cf99')
