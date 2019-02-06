import calendar


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    # calendar is nice, but you can also use: date.strftime('%A')
    weekday = date.weekday()
    return calendar.day_name[weekday]