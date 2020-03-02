from datetime import date


def firstrun():
    return "success"


def circleArea(radius):
    area = 2 * 3.14 * radius
    return area


def listLast(list):
    size = len(list)
    last = size-1
    return list[last]


def dateDiff(date1, date2):
    yearDiff = date1.year() - date2.year()
    monthDiff = date1.month() - date2.month()
    dayDiff = date1.day() - date2.day()
    dateSub = (yearDiff * 365) + (monthDiff * 30) + dayDiff
    return dateSub
