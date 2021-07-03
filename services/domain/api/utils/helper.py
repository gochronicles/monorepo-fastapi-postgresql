from datetime import datetime


def parse_date(date: str):
    try:
        date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        date_str = date.strftime("%Y-%m-%d %H:%M:%S")
        return date, date_str
    except ValueError as error:
        raise error


def validate_date(start_date: datetime.date, end_date: datetime.date):
    try:
        today = datetime.now()
        return today < start_date or today < end_date or end_date < start_date
    except ValueError as error:
        raise error
