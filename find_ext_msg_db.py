# -*- coding: utf-8 -*-

"""
Create at 16/11/15

Select * From MAIN.[Files] where
[domain] like '%tencent%xin%'
and [relativePath] like '%dee6%'
and [relativePath] not like '%pic%'
and [relativePath] not like '%aud%'
and [relativePath] not like '%video%'
and [relativePath] not like '%xls%'
and [relativePath] not like '%xlsx%'
and [relativePath] not like '%docx%'
and [relativePath] not like '%Img%'
and [relativePath] not like '%opendata%'
and [relativePath] not like '%session%'
and [relativePath] not like '%translate%'
and [relativePath] not like '%pattern_v3%'

"""

__author__ = 'TT'

import os

dir_name = 'E:/Eileen/eeee'
tar_name = 'E:/Eileen/eeee-bak'


for root, dirs, files in os.walk(dir_name):

    for name in files:
        if '.' in name:
            continue
        if not os.path.exists(os.path.join(tar_name, name[:2], name)):
            print os.path.join(root, name), file_size, 'None not exists'
            continue
            # shutil.copy(os.path.join(root, name), os.path.join(tar_name, name[:2], name))

        file_size = os.path.getsize(os.path.join(root, name))
        tar_size = os.path.getsize(os.path.join(tar_name, name[:2], name))
        if file_size != tar_size:
            print os.path.join(root, name), file_size, tar_size, 'diff'
            # shutil.copy(os.path.join(root, name), os.path.join(tar_name, name[:2], name))