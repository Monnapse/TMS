from tms import period_times, timestamp_seconds, timestamp_times, time

# Period times
print(period_times.days_year) # 365
print(period_times.days_month) # 30
print(period_times.days_week) # 7
print(period_times.hours_day) # 24
print(period_times.minute_hour) # 60
print(period_times.seconds_minute) # 60

# Timestamp times in seconds
print(timestamp_seconds.hour) # 3600
print(timestamp_seconds.day) # 86400
print(timestamp_seconds.week) # 604800
print(timestamp_seconds.month) # 2592000
print(timestamp_seconds.year) # 31536000

# Calculate custom timestamp seconds
print(timestamp_times.minutes(2)) # 120
print(timestamp_times.hours(2)) # 7200
print(timestamp_times.days(2)) # 172800
print(timestamp_times.weeks(2)) # 1209600
print(timestamp_times.months(2)) # 5184000
print(timestamp_times.years(2)) # 63072000

# Calculate custom timestamp seconds
print(time.now()) # 1709861189
print(time.minutes(2)) # 1709861069
print(time.hours(2)) # 1709853989
print(time.days(2)) # 1709688389
print(time.weeks(2)) # 1708651589
print(time.months(2)) # 1704677189
print(time.years(2)) # 1646789189