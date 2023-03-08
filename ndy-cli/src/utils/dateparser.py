import parsedatetime

from datetime import datetime


def dateparser(raw_date):
    cal = parsedatetime.Calendar()

    time_struct, parse_status = cal.parse(raw_date)
    date = datetime(*time_struct[:6])
    return date
