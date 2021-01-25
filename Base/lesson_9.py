# массив=список в пайтоне
list = []
print(list)
list = ['h', 'e', 'l', 'l', 'o']
print(list)

print(list[0])
print(list[1])
print("Последний элемент: ", list[-1])
print("Последний элемент :", list[len(list) - 1])
print("Длина массива = кол-во элементов в массиве: ", len(list))
print("----------------------------------")

i = 0
while i < len(list):
    print(list[i])
    i += 1

list = ['a', 3, 5.7, True]
i = 0
while i < len(list):
    print(list[i])
    i += 1
list[1] = 'b'
print(list[1])
list[3] = False
print(list[len(list) - 1])
print("----------------------------------")
list = [[2, 3], 4]
print(list[0][0])
print(list[0][1])
print(list[1])
print("----------------------------------")

list = [[2, 3], [4, 5, 6]]  # перебор многомерного массива
i = 0
while i < len(list):
    j = 0
    while j < len(list[i]):
        print(list[i][j])
        j += 1
    i += 1
print("----------------------------------")

prices = [20, 30, 15, 20, 45, 15]
min = prices[0]
max = prices[0]
i = 1
while i < len(prices):
    if prices[i] < min:
        min = prices[i]
    if prices[i] > max:
        max = prices[i]
    i += 1
print("Array:", prices)
print("min =", min)
print("max =", max)
print("----------------------------------")

# exercise
arr = ['first', 'second', 'third', 'fourth']
i = 0
while i < len(arr):
    print('Значение ', i, 'ого элемента =', arr[i])
    i += 1
chooseEl = int(input('Введите индекс элемента массива 0-3 :'))
if chooseEl < len(arr):
    print('Значение элемента под индексом', chooseEl, ' = ', arr[chooseEl])
else:
    print('Элемента с таким индексом не существует!')
