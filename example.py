from tms import period_times, time_type, timestamp_times, time, time_direction

# Period times
print(period_times.days_year) # 365
print(period_times.days_month) # 30
print(period_times.days_week) # 7
print(period_times.hours_day) # 24
print(period_times.minute_hour) # 60
print(period_times.seconds_minute) # 60

# Timestamp times in seconds
print(time_type.minute) # 60
print(time_type.hour) # 3600
print(time_type.day) # 86400
print(time_type.week) # 604800
print(time_type.month) # 2592000
print(time_type.year) # 31536000

# Calculate custom timestamp seconds
print(timestamp_times.time(2, time_type.minute)) # 120
print(timestamp_times.time(2, time_type.hour)) # 7200
print(timestamp_times.time(2, time_type.day)) # 172800
print(timestamp_times.time(2, time_type.week)) # 1209600
print(timestamp_times.time(2, time_type.month)) # 5184000
print(timestamp_times.time(2, time_type.year)) # 63072000

# Calculate custom timestamp seconds
print(time.now()) # 1709862028
print(time.time(2, time_type.minute, time_direction.before)) # 1709861908
print(time.time(2, time_type.hour, time_direction.before)) # 1709854828
print(time.time(2, time_type.day, time_direction.before)) # 1709689228
print(time.time(2, time_type.week, time_direction.before)) # 1708652428
print(time.time(2, time_type.month, time_direction.before)) # 1704678028
print(time.time(2, time_type.year, time_direction.before)) # 1646790028