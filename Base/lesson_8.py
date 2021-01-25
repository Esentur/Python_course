# циклы
i = 0
while i < 10:
    # i=i+1
    print("Hello World!", i)
    i += 1
print("Цикл завершен")
print("-------------")

i = 0
while i < 10:
    i += 1
    print(i)

print("-------------")

i = 0
while i < 10:
    i += 1
    # if i!=5:
    #    print(i)
    if i == 5:
        continue
    if i == 8:
        break
    print(i)
print("Цикл завершен. i =", i)

print("-------------")

x = 1
s = 0
to = 10
while x <= to:
    s += x
    x += 1
print("Сумма чисел от 1 до", to, "равна", s)

print("-------------")

while True:
    code = input("Введите 0 для выхода")
    if code == "0":
        break

print("-------------")

# exercise
sum = 0
while True:
    num = input("Команды: ввод числа, sum, exit")
    if num == "sum":
        print(sum)
        num = 0
        sum = 0
    if num == "exit" or num == "quit":
        break
    sum = sum + int(num)
