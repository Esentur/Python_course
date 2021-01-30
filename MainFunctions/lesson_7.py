from datetime import *
from time import *

print(date.today())
print(datetime.today())

d = date(2025, 7, 15)
print(d)

dt = datetime(1998, 10, 22, 8, 30, 00)
print(dt)

print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print('------------------------')
print(dt.strftime('%Y.%m.%d %H:%M:%S'))
print(dt.strftime('%Y/%m/%d %H:%M:%S'))
print('------------------------')
print(time())  # сколько секунд прошло с 1970 ответ это "настоящее датавремя только в секундах"

dt = datetime.fromtimestamp(time())  # получаем дату время в 1 значении
print(dt)
print(dt.year)  # потом можно разобрать по частям
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)

print(dt.timestamp())
start = time()
i = 0
while i < 100000:
    i += 1
print("Время выполнения скрипта: ", time() - start)

print('------------------------')
print('exercise')
now = date.today()
then = date(1998, 10, 22)
delta = now - then
print(delta)
import datetime, time
# сколько секунд ты прожил
# d = input('Example: 2020-01-31\n')
# year, month, day = map(int, d.split('-'))
# birth_date = datetime.date(year, month, day)
# total_date = datetime.datetime.now()
# print(time.mktime(total_date.timetuple()) - time.mktime(birth_date.timetuple()))
