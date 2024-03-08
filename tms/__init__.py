"""
    Made by Monnapse

    Get timestamp seconds for dates/times, seconds minutes, hours, days, weeks, months, years.
"""

class period_times:
    days_year = 365 # Days in a year
    days_month = 30 # Days in a month
    days_week = 7 # Days in a week
    hours_day = 24 # Hours in a day
    minute_hour = 60 # Minutes in an hour
    seconds_minute = 60 # Seconds in a minute

class timestamp_times:
    """
        Period times in seconds, for timestamp
    """
    hour = period_times.minute_hour * period_times.seconds_minute # Seconds in an hour
    day = period_times.hours_day * period_times.minute_hour * period_times.seconds_minute # Seconds in a day
    week = period_times.days_week * period_times.hours_day * period_times.minute_hour * period_times.seconds_minute # Seconds in a week
    month = period_times.days_month * period_times.hours_day * period_times.minute_hour * period_times.seconds_minute # Seconds in a week
    year = period_times.days_year * period_times.hours_day * period_times.minute_hour * period_times.seconds_minute # Seconds in a year

class time:
    def minutes(amount: float | None=0):
        return amount * period_times.seconds_minute
    def hours(amount: float | None=0):
        return amount * timestamp_times.hour
    def days(amount: float | None=0):
        return amount * timestamp_times.day
    def week(amount: float | None=0):
        return amount * timestamp_times.week
    def month(amount: float | None=0):
        return amount * timestamp_times.month
    def year(amount: float | None=0):
        return amount * timestamp_times.year