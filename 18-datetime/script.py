"""
datetime_example.py

This file demonstrates the basics of Python's datetime module.

Topics covered:
1. Current date and time
2. Creating dates
3. Formatting dates
4. Parsing strings
5. Date arithmetic
6. Comparing dates
7. Working with timestamps
"""

from datetime import datetime, date, time, timedelta

# --------------------------------------------------
# 1. Current date and time
# --------------------------------------------------

print("=== Current Date and Time ===")

now = datetime.now()

print("Current datetime:", now)
print("Current date:", now.date())
print("Current time:", now.time())

print()


# --------------------------------------------------
# 2. Creating a datetime object
# --------------------------------------------------

print("=== Creating Dates ===")

birthday = datetime(1995, 8, 15, 10, 30, 0)

print("Birthday:", birthday)

print()


# --------------------------------------------------
# 3. Creating only a date
# --------------------------------------------------

print("=== Date Object ===")

today = date.today()

print(today)

print()


# --------------------------------------------------
# 4. Creating only a time
# --------------------------------------------------

print("=== Time Object ===")

meeting = time(14, 45)

print(meeting)

print()


# --------------------------------------------------
# 5. Formatting datetime
# --------------------------------------------------

print("=== Formatting Dates ===")

print(now.strftime("%Y-%m-%d"))
print(now.strftime("%m/%d/%Y"))
print(now.strftime("%B %d, %Y"))
print(now.strftime("%A"))
print(now.strftime("%I:%M %p"))
print(now.strftime("%Y-%m-%d %H:%M:%S"))

print()


# Common formatting codes
#
# %Y -> 2026
# %y -> 26
# %m -> Month (01-12)
# %d -> Day (01-31)
# %H -> Hour (24-hour)
# %I -> Hour (12-hour)
# %M -> Minute
# %S -> Second
# %A -> Monday
# %B -> January


# --------------------------------------------------
# 6. Parsing a string into datetime
# --------------------------------------------------

print("=== Parsing Strings ===")

text = "2026-07-25 18:30"

parsed = datetime.strptime(text, "%Y-%m-%d %H:%M")

print(parsed)

print()


# --------------------------------------------------
# 7. Date arithmetic
# --------------------------------------------------

print("=== Date Arithmetic ===")

today = datetime.now()

tomorrow = today + timedelta(days=1)

yesterday = today - timedelta(days=1)

next_week = today + timedelta(weeks=1)

after_three_hours = today + timedelta(hours=3)

print("Today:       ", today)
print("Tomorrow:    ", tomorrow)
print("Yesterday:   ", yesterday)
print("Next Week:   ", next_week)
print("3 Hours Later:", after_three_hours)

print()


# --------------------------------------------------
# 8. Difference between dates
# --------------------------------------------------

print("=== Difference Between Dates ===")

start = datetime(2026, 1, 1)

end = datetime(2026, 12, 31)

difference = end - start

print("Difference:", difference)
print("Days:", difference.days)

print()


# --------------------------------------------------
# 9. Comparing dates
# --------------------------------------------------

print("=== Comparing Dates ===")

d1 = datetime(2026, 5, 1)

d2 = datetime(2026, 6, 1)

print(d1 < d2)
print(d1 > d2)
print(d1 == d2)

print()


# --------------------------------------------------
# 10. Unix timestamp
# --------------------------------------------------

print("=== Timestamp ===")

timestamp = now.timestamp()

print("Unix Timestamp:", timestamp)

restored = datetime.fromtimestamp(timestamp)

print("Converted back:", restored)

print()


# --------------------------------------------------
# 11. Practical Example
# --------------------------------------------------

print("=== Practical Example ===")

deadline = datetime(2026, 12, 31)

remaining = deadline - datetime.now()

print(f"Days until deadline: {remaining.days}")

print()


# --------------------------------------------------
# 12. Loop through future dates
# --------------------------------------------------

print("=== Next 7 Days ===")

today = datetime.now()

for i in range(7):
    future = today + timedelta(days=i)
    print(future.strftime("%A, %Y-%m-%d"))

print()


# --------------------------------------------------
# 13. Birthday calculation
# --------------------------------------------------

print("=== Age Calculation Example ===")

birthday = datetime(1995, 8, 15)

today = datetime.now()

age = today.year - birthday.year

# Has birthday occurred yet this year?
if (today.month, today.day) < (birthday.month, birthday.day):
    age -= 1

print("Age:", age)

print()


# --------------------------------------------------
# 14. Formatting examples
# --------------------------------------------------

print("=== More Formatting Examples ===")

formats = [
    "%Y-%m-%d",
    "%d/%m/%Y",
    "%m/%d/%Y",
    "%B %d, %Y",
    "%b %d",
    "%A",
    "%I:%M %p",
    "%H:%M:%S",
]

for f in formats:
    print(f"{f:15} -> {now.strftime(f)}")
