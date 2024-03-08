from tms import period_times, timestamp_times, time

# Period times
print(period_times.days_year) # 365
print(period_times.days_month) # 30
print(period_times.days_week) # 7
print(period_times.hours_day) # 24
print(period_times.minute_hour) # 60
print(period_times.seconds_minute) # 60

# Timestamp times in seconds
print(timestamp_times.hour) # 3600
print(timestamp_times.day) # 86400
print(timestamp_times.week) # 604800
print(timestamp_times.month) # 2592000
print(timestamp_times.year) # 31536000

# Calculate custom timestamp seconds
print(time.minutes(2)) # 120
print(time.hours(2)) # 7200
print(time.days(2)) # 172800
print(time.week(2)) # 1209600
print(time.month(2)) # 5184000
print(time.year(2)) # 63072000