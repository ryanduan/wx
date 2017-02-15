# -*- coding: utf-8 -*-

"""
Create at 16/12/2
"""

__author__ = 'TT'

from biplist import *
import os
import time

tar_dir = 'exc_m'

# plist = readPlist('2222.ichat')

# print plist


def time_strap(t):
    nt = 978307200
    ts = nt + int(t)
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))


# print plist
def ana_ichat(plist):
    for k in plist['$objects']:
        # print k, type(k)
        # print k
        if isinstance(k, dict):
            # print k
            if 'NS.time' in k.keys():
                t = k['NS.time']
                print '\t',
                print time_strap(t)
            # if isinstance(k.get('NS.string', None), unicode):
            if 'NS.string' in k.keys():
                print '\t',
                print k['NS.string'], 1
        if isinstance(k, unicode):
            print '\t',
            print k
            # elif isinstance(k, dict):


for r, d, fl in os.walk(tar_dir):
    n = True
    for f in fl:
        if f.startswith('.'):
            continue
        # print f
        try:
            print os.path.join(r, f)
            # f = f.replace('?', '')
            plist = readPlist(os.path.join(r, f))
            # print plist
            ana_ichat(plist)
        except:
            import traceback
            print traceback.format_exc()
            n = False
            print '===================='
            # break
            continue
    # if not n:
    #     break


# ana_ichat(plist)
