# 关于确定星期几 没想到比较好的方法，如果想到了说不定可以解决1-6个点
from datetime import datetime, date


def get_all():
    tmp = input().split(' ')
    line_numbers = int(tmp[0])
    start_time, end_time = tmp[1], tmp[2]
    start_year, start_month, start_day, start_hour, start_minutes = \
        int(start_time[0:4]), int(start_time[4:6]), int(start_time[6:8]), int(start_time[8:10]), int(start_time[10:12])
    end_year, end_month, end_day, end_hour, end_minutes = \
        int(end_time[0:4]), int(end_time[4:6]), int(end_time[6:8]), int(end_time[8:10]), int(end_time[10:12])
    for i in range(line_numbers):
        tmp = input().split(' ')
        year, month, day, hour, minute, thing = tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5]


get_all()
