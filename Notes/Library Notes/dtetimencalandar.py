import calendar

yy = 1917
mm = 11

print(calendar.month(yy, mm))

print("The calandar of year 2023 is: ")
print(calendar.calendar(2023))

# formatting
print(calendar.calendar(2023, 2, 1, 6, 1))

import datetime
current_time = datetime.datetime.now()
print(current_time)

print(f"year: {current_time.year}")
print(f"month: {current_time.month}")
print(f"day: {current_time.day}")
print(f"minute: {current_time.minute}")
print(f"second: {current_time.second}")

from datetime import date
today = date.today()
print(today)

from datetime import datetime
time = datetime.now().time()
print(f"current time is: {time}")
