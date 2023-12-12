import datetime


def today():
    return datetime.datetime.now()


def count_days(date1,date2=today()):
    if isinstance(date1,datetime.timedelta):
        if isinstance(date2,datetime.timedelta):
            return date1 - datetime.timedelta(date2)