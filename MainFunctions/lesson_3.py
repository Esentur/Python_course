# Основные функции для списков и кортежей
list = [1, 2, 0, 5]
list[0] = 7
print(list)
print(len(list))
list.append(9)  # +1 в конец
print(list)

list.extend([0, 1])  # +несколько в конец
print(list)

list.insert(0, 5)  # +в указанный индекс(позицию) т.е в [0] поставь значение '5'
print(list)
print('----------')

print(list.index(0))  # находит индекс значениЯ 0
print(list.index(0, 4))  # находит индекс значениЯ 0 начав поиск с 4

print(list.count('a'))  # сколько раз встречается
print(list.count(0))  # счетчик сколько раз встречается
print('----------')

list.reverse()
print(list)
print('----------')

list.remove(0)  # удаляем элемент со значением 0 первый встретившийся
print(list)
list.pop(3)  # удаляет элемент с указанным индексом
print(list)
list.clear() # удалить все элементы
print(list)
print('----------')

list =[1,3,0,5,1]
list.sort()
print(list)
list.sort(reverse=True)
print(list)
print('----------')

#все операции со списками работают и с кортежами за искл-м операции редак-я
mytuple=tuple('hello')
print('наш кортеж-неизм.список : ', mytuple)
print('находим индекс элемента со значением "е" ---',mytuple.index('e'))
print('выводим значение элемента под индексом [0] ----',mytuple[0])
print('сколько раз встречается значение "l" у элементов ---', mytuple.count('l'))
print('------------------------------------')
#exercise
print('exercise')

length=int(input('Введите размер списка :'))
newarr=[]
i=0
while i<length:
    print('Введите значение элемента ',i,':')
    num=input()
    newarr.append(num)
    i+=1
print(newarr)

