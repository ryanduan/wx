# -*- coding: utf-8 -*-

"""
Create at 16/10/28
"""

__author__ = 'TT'

import os
import shutil

dir_name = 'E:/Eileen/755cdd10ae12a8b57f756cb33373007638c183fe'
tar_name = 'E:/Eileen/755cdd10ae12a8b57f756cb33373007638c183fe'


for root, dirs, files in os.walk(dir_name):

    for name in files:
        print root
        file_size = os.path.getsize(os.path.join(root, name))
        if not os.path.exists(os.path.join(tar_name, name[:2], name)):
            print os.path.join(root, name), file_size, 'None'
            shutil.copy(os.path.join(root, name), os.path.join(tar_name, name[:2], name))
        tar_size = os.path.getsize(os.path.join(tar_name, name[:2], name))
        if file_size != tar_size:
            print os.path.join(root, name), file_size, tar_size
            shutil.copy(os.path.join(root, name), os.path.join(tar_name, name[:2], name))


