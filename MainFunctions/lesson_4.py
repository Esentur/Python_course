#  Основные функции для работы со множествами set
from random import *
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4}

print(len(set1))

set1.add(10)
set1.add(10)
print(set1)

set1.remove(10)
print(set1)

# set1.remove(5)ошибк т.к. нет элемента со значением 5
set1.discard(5)
print(set1)
print('-------------------')

# сравнение
print(set1 == set2)
print(set1 <= set2)
print(set1 >= set2)
print(set2 >= set1)
print('-------------------')

set1={1,2,3,4}
set1={1,2,3}

print(set1.union(set2)) # объединение
print(set1.intersection(set2)) #пересечение/ элементы есть в обоих множествах
print(set2.difference(set1)) # разница в set2 нет 4 чем set1

set1.clear()
set2.clear()
print(set1, set2)
print('-------------------')
#exercise
print('exercise')

myset1={randint(1,10) for i in range(10)}
print(myset1)
myset2={randint(1,10) for i in range(10)}
print(myset2)

print('Объединение :',myset1.union(myset2))
print('Пересечение(Общие элементы) :',myset1.intersection(myset2))
print('Разница :',myset1.difference(myset2))
