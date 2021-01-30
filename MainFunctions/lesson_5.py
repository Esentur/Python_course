from random import *

# Основные функции для работы со словарями
d = {'name': 'Alex', 'age': 35}
print(d)
print('----------------')
d.setdefault('isWorking', True)
print(d)
print(d.get('age'))
d.pop('name')
print(d)
print('----------------')

print(d.keys())
keys = list(d.keys())
print(keys[0])
print('----------------')

print(d.values())
values = list(d.values())
print(values[0])

d['age'] = 40
d['isMale'] = True
print(d)

d.clear()
print(d)
print('-----------------------')
print('exercise')

mydict = dict(Hello='Привет', Bye='Пока', Lesson='Урок')
keysarr = list(mydict.keys())
valuesarr = list(mydict.values())

while True:
    randNum = randint(0, 2)
    #print('Рандомный индекс :', randNum)
    quest = valuesarr[randNum]
    trueAns = keysarr[randNum]
    print('show - вывести словарь или quit - завершить программу\n'
          'или же как будет на английском :', quest, '?\n')
    ans = input()
    if ans == 'show':
        print(mydict)
    elif ans == 'quit':
        break
    elif ans.lower() == trueAns.lower():
        print('Верно')
    else:
        print('Некорректный ввод')
