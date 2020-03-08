import arrow

utc = arrow.utcnow()

print(utc)

utc = utc.replace(month=1)
print(utc)

date = arrow.utcnow()
print(date)
date = date.shift(hours=-1)
print(date)
print(date.humanize())