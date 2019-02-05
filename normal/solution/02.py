import datetime


def business_days(start_date, num):
    result = []

    while len(result) < num:
        if start_date.weekday() < 5:
            result.append(start_date)

        start_date += datetime.timedelta(1)

    return result
