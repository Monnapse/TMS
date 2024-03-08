"""
    Made by Monnapse

    Get timestamp seconds for dates/times, seconds minutes, hours, days, weeks, months, years.
"""

import time as t

class period_times:
    days_year = 365 # Days in a year
    days_month = 30 # Days in a month
    days_week = 7 # Days in a week
    hours_day = 24 # Hours in a day
    minute_hour = 60 # Minutes in an hour
    seconds_minute = 60 # Seconds in a minute

class timestamp_seconds:
    """
        Period times in seconds, for timestamp
    """
    hour = period_times.minute_hour * period_times.seconds_minute # Seconds in an hour
    day = period_times.hours_day * period_times.minute_hour * period_times.seconds_minute # Seconds in a day
    week = period_times.days_week * period_times.hours_day * period_times.minute_hour * period_times.seconds_minute # Seconds in a week
    month = period_times.days_month * period_times.hours_day * period_times.minute_hour * period_times.seconds_minute # Seconds in a week
    year = period_times.days_year * period_times.hours_day * period_times.minute_hour * period_times.seconds_minute # Seconds in a year

class timestamp_times:
    def minutes(amount: float | None=0) -> int:
        """
            Returns seconds in amount minutes
        """
        return amount * period_times.seconds_minute
    def hours(amount: float | None=0) -> int:
        """
            Returns seconds in amount hours
        """
        return amount * timestamp_seconds.hour
    def days(amount: float | None=0) -> int:
        """
            Returns seconds in amount days
        """
        return amount * timestamp_seconds.day
    def weeks(amount: float | None=0) -> int:
        """
            Returns seconds in amount weeks
        """
        return amount * timestamp_seconds.week
    def months(amount: float | None=0) -> int:
        """
            Returns seconds in amount months
        """
        return amount * timestamp_seconds.month
    def years(amount: float | None=0) -> int:
        """
            Returns seconds in amount years
        """
        return amount * timestamp_seconds.year
    
class time:
    def now() -> int:
        """
            Returns the current time in seconds since the Epoch.
        """
        return int(t.time())
    def minutes(amount: float | None=0) -> int:
        """
            Returns the current time in seconds since the Epoch subtracted by seconds in amount minutes
        """
        return time.now() - timestamp_times.minutes(amount)
    def hours(amount: float | None=0) -> int:
        """
            Returns the current time in seconds since the Epoch subtracted by seconds in amount hours
        """
        return time.now() - timestamp_times.hours(amount) 
    def days(amount: float | None=0) -> int:
        """
            Returns the current time in seconds since the Epoch subtracted by seconds in amount days
        """
        return time.now() - timestamp_times.days(amount) 
    def weeks(amount: float | None=0) -> int:
        """
            Returns the current time in seconds since the Epoch subtracted by seconds in amount weeks
        """
        return time.now() - timestamp_times.weeks(amount) 
    def months(amount: float | None=0) -> int:
        """
            Returns the current time in seconds since the Epoch subtracted by seconds in amount months
        """
        return time.now() - timestamp_times.months(amount) 
    def years(amount: float | None=0) -> int:
        """
            Returns the current time in seconds since the Epoch subtracted by seconds in amount years
        """
        return time.now() - timestamp_times.years(amount) 