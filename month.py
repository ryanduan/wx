# -*- coding: utf-8 -*-

"""
Create at 16/11/17
"""

__author__ = 'TT'

from dateutil.relativedelta import relativedelta
import datetime
import calendar


def last_day(dt, forward=0):
    return datetime.date(dt.year, dt.month, calendar.monthrange(dt.year, dt.month)[-1] - forward)


def rrule_monthly1(start_time, end_time, pay_method_f=1, start_num=0):
    """    将 start_time 到 end_time 的时间段分成按付款周期的时间段    """
    if start_time + relativedelta(months=pay_method_f) > end_time:
        yield (1 + start_num, start_time, end_time)
    else:
        months = (end_time.year - start_time.year) * 12 + end_time.month - start_time.month
        i = j = -1
        for j, i in enumerate(range(0, months, pay_method_f)):

            current_time = start_time + relativedelta(months=i)
            if start_time == last_day(start_time):
                current_time = last_day(current_time)
            current_end_time = start_time + relativedelta(months=i + pay_method_f, days=-1)
            # print current_time, last_day(current_time)
            if current_time == last_day(current_time):
                current_end_time = last_day(current_end_time, 1)
                print current_end_time, 2
            else:
                current_end_time = min(current_end_time, end_time)
            # print current_time, current_end_time, i, 1
            yield (j + 1 + start_num, current_time, current_end_time)
        else:
            # print start_time, start_time + relativedelta(months=i + pay_method_f), 3, i
            current_time = start_time + relativedelta(months=i + pay_method_f)
            if current_time <= end_time:
                current_end_time = start_time + relativedelta(months=i + pay_method_f + 1, days=-1)
                current_end_time = min(current_end_time, end_time)
                print current_time, current_end_time, i, 2
                yield (j + 2 + start_num, current_time, current_end_time)


def rrule_monthly(start_time, end_time, pay_method_f=1, start_num=0):
    """    将 start_time 到 end_time 的时间段分成按付款周期的时间段    """
    if start_time + relativedelta(months=pay_method_f) > end_time:
        yield (1 + start_num, start_time, end_time)
    else:
        months = (end_time.year - start_time.year) * 12 + end_time.month - start_time.month
        i = j = -1
        for j, i in enumerate(range(0, months, pay_method_f)):
            current_time = start_time + relativedelta(months=i)
            current_end_time = start_time + relativedelta(months=i + pay_method_f, days=-1)
            current_end_time = min(current_end_time, end_time)
            print current_time, current_end_time, i, 1
            yield (j + 1 + start_num, current_time, current_end_time)
        else:
            # print start_time, start_time + relativedelta(months=i + pay_method_f), 3, i
            current_time = start_time + relativedelta(months=i + pay_method_f)
            if current_time <= end_time:
                current_end_time = start_time + relativedelta(months=i + pay_method_f + 1, days=-1)
                current_end_time = min(current_end_time, end_time)
                print current_time, current_end_time, i, 2
                yield (j + 2 + start_num, current_time, current_end_time)


st = datetime.datetime.strptime('2016-2-29', '%Y-%m-%d').date()
et = datetime.datetime.strptime('2017-2-27', '%Y-%m-%d').date()
# 2016-12-31 2017-12-30
# for i, i_start, i_end in rrule_monthly(st, et):
#     print i, i_start, i_end, 'A'

#
for i in rrule_monthly1(st, et):
    print i, 'B'

# print st + relativedelta(months=1)