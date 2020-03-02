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
    dateA = date(date1.year(), date1.month(), date1.day())
    dateB = date(date2.year(), date2.month(), date2.day())
    yearDiff = dateA.year() - dateB.year()
    monthDiff = dateA.month() - dateB.month()
    dayDiff = dateA.day() - dateB.day()
    dateSub = (yearDiff * 365) + (monthDiff * 30) + dayDiff
    return dateSub
