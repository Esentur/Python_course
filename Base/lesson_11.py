# множества
# не могут содержать одинаковые элементы, каждый элемент уникален
# нет порядка.каждый раз элементы меняют порядок
import random

mySet = set()
print(mySet)
mySet2 = {}
print(mySet2)

mySet = set("Pythonnn")
print(mySet)

mySet2 = {'1', 2, 3, 1, '1'}
print(mySet2)

print(int(random.random() * 10))
# рандомный массив -> преоб-м во множество исключив повторения. потом обратно преоб-м в массив

arr = [int(random.random() * 10) for i in range(0, 10)]
print(arr)
arr = list(set(arr))
print(arr)
print("----------------------------------")
# exercise

length = int(input("Введите количество элементов списка: "))
myArr = [int(random.random() * 10) for i in range(0, length)]
print("Ваш список размером в", length, "элементов сгенерирован случайными числами от 0-10:  \n")
print(myArr)
m = 0
while m < len(myArr):
    print(m, "й элемент ---", myArr[m])
    m += 1

myArr = list(set(myArr))  # list-set-list
i = 0
for i in myArr:
    print(i)
print("Длина конечного списка без повторяющихся элементов :", len(myArr))
