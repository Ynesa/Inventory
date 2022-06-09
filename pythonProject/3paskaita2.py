import datetime
x = datetime.datetime.today()
print(x)
now = datetime.datetime.now()
print(now - datetime.timedelta(days=5))
x = datetime.datetime.today()
print(now + datetime.timedelta(hours=8, days=8))