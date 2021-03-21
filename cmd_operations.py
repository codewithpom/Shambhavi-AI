import os


def set_time(hour, minute, second=0):
    hour = str(hour)
    minute = str(minute)
    second = str(second)
    total_time = hour+':'+minute+':' + second
    os.system('time '+total_time)
    return 'Successfully changed time'


def set_date(day, month, year):
    day = str(day)
    month = str(month)
    year = str(year)
    os.system('date '+month+'-'+day+'-'+year)
    return 'Successfully changed date'
