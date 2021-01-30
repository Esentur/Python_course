# Основные математические функции
from math import *

print(e)
print(pi)
print('---------------')

print(sin(1))
print(cos(1))
print(tan(1))
print(1 / tan(1))
print('---------------')

print(sin(radians(30)))  # перевести в градусы. по умолчанию это радианы
print(cos(radians(60)))  # перевести в градусы. по умолчанию это радианы
print(degrees(1))  # перевести радианы в градусы.
print('---------------')

print(fabs(-5))  # модуль числа
print(floor(5.9))  # -к целому
print(ceil(5.1))  # +к целому
print(sqrt(9))  # квадратный корень
print('---------------')

print(round(5.2))  # округление классическое
print(round(5.5))
print(round(5.387, 2))
print(round(5 / 7, 3))
print('---------------')
# exercise
print('exercise')
print(round(13 / 17, 2))
i = 0
for i in range(181):
    print('sin(', i, ') градусов =', round(sin(radians(i)), 4))
    i += 1
