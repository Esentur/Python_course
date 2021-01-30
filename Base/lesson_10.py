# цикл for(each) и генераторы списков
# для каждого

array = [1, 5, 0, -5, 2.5]
for n in array:
    print(n)
print("------------")

str = 'Python'
print(str[0])

for s in str:
    print(s)

for s in str:  # for else
    if s == "Y":
        break
else:
    print("Символа Y в строке", str, "нет.")
print("------------")

array = list(range(2, 15))  # не является списком. range другой тип данных
print(array[0])
for n in array:
    print(n)
print("------------")

array = [i for i in range(1, 10)]
print(array)
array = [i * 2 for i in range(1, 10)]
print(array)
array = [i for i in range(1, 10) if i % 2 == 0]
print(array)
print("------------")

# exercise

arr = list(range(0, 5))
print(arr)
for n in arr:
    print(n)


i = 0
sum = 0
while i < len(arr):
    sum += arr[i]
    i += 1
avr = sum / len(arr)
print("Сумма элементов массива :", sum)
print("Среднее арифмитическое элементов массива :", avr)
# теперь с циклом for
arr1 = list(range(0, 5))
print(arr1)
for n in arr:
    print(n)


sum1 = 0
for m in arr1:
    sum1 += arr[m]
    m += 1
print("Сумма элементов массива :", sum1)
print("Среднее арифмитическое элементов массива :", sum1 / len(arr))
