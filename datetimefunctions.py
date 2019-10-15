import datetime
import random
import calendar
from time import mktime

def getDateSignature():
    return str(datetime.datetime.now().date().year) + \
    ("00" + str(datetime.datetime.now().date().month))[-2:] + \
    ("00" + str(datetime.datetime.now().date().day))[-2:]

def getTimeSignature():
    return ("00" + str(datetime.datetime.now().time().hour))[-2:] + \
        ("00" + str(datetime.datetime.now().time().minute))[-2:] + \
        ("00" + str(datetime.datetime.now().time().second))[-2:]

def getDateTimeSignature():
    return getDateSignature() + getTimeSignature()

def getRandomSignature(minimum, maximum):
    longitud = len(str(maximum))
    return ("0" * longitud + str(random.randint(minimum, maximum + 1)))[-longitud:]

def getDateTimeRandomSignature():
    return getDateSignature() + getTimeSignature() + getRandomSignature(1, 10000)

def getTodayAsDatetime():
    return datetime.datetime.now()

def get_today_as_date():
    current_time = datetime.datetime.today()
    return datetime.datetime.strptime(str(current_time), '%d/%m/%Y').date()

def getSecondsBetween(dateIni, dateEnd):
    return getSecondsSinceEpoch(dateEnd) - getSecondsSinceEpoch(dateIni)

def getSecondsSinceEpoch(date):
    par_year = date.year
    par_month = date.month
    par_day = date.day

    par_hour = 0
    par_minutes = 0
    par_seconds = 0
    par_milliseconds = 0

    t = (par_year, par_month, par_day, par_hour, par_minutes, par_seconds, par_milliseconds, 0, 0)

    return mktime(t)

def getDateAddingMonths(initialdate, months):
    month = initialdate.month - 1 + months
    year = initialdate.year + month
    month = month % 12 + 1
    day = min(initialdate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)
