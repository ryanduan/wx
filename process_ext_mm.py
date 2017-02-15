# -*- coding: utf-8 -*-

"""
Create at 16/11/15

fts_message.db

"""

__author__ = 'TT'

import sqlite3
import time


tar_dir = '161208'
db = '5dc5f02063930d7b30a1db9065705f3d88e2201f'


def format_timestamp(ts):
    """"""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))


class WX(object):
    conn = sqlite3.connect('{}/{}'.format(tar_dir, db))

    def __init__(self):
        pass

    def list_tb(self):
        res = self.conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
        ret = res.fetchall()
        return [i[0] for i in ret if i[0].endswith('content') and i[0].startswith('fts_message')]

    def get_msg(self, tb):
        res = self.conn.execute("select c0usernameid, c1MesLocalID, c2CreateTime, c3Message FROM {}".format(tb))
        ret = res.fetchall()
        # s_set = set([i[-1] for i in ret])
        # if len(s_set) == 1:
        #     return []
        return ret

    def get_user(self):
        res = self.conn.execute("select usernameid, UsrName FROM fts_username_id")
        ret = res.fetchall()
        return dict(ret)


wx = WX()
tbs = wx.list_tb()
uid_dict = wx.get_user()
ext_msg_dict = dict()
for tb in tbs:
    msg = wx.get_msg(tb)
    c = ''
    if not msg:
        continue
    for u, i, t, m, in msg:
        d = format_timestamp(t)
        un = '{}-{}'.format(u, uid_dict.get(u))
        n = '{}-{}:{}'.format(tb, d, m.encode('utf-8'))
        if un in ext_msg_dict.keys():
            ext_msg_dict[un].append(n)
        else:
            ext_msg_dict[un] = [n]


for k, v in ext_msg_dict.items():
    if k.endswith('chatroom'):
        continue
    target = '{}/ext_msg/{}.txt'.format(tar_dir, k)
    writer = open(target, 'w')
    if v:
        c = '\n'.join(v)
        writer.write(c)
        writer.close()
