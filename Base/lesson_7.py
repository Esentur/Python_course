# условные операторы
print("Введите 0, 1 или 2:")
a = input()
if a == "0":
    print("Вы ввели НОЛЬ")
elif a == "1":
    print("Вы ввели ОДИН")
elif a == "2":
    print("Вы ввели ДВА")
else:
    print("Некорректный ввод")

cond = a == "0" or a == "1" or a == "2"

if cond:
    x = 1
else:
    x = 0
print("x =", x)

x = 1 if cond else 0
print("x =", x)

# exercise
print("Exercise: ---------------------")
num1 = int(input("Введите 1ое число:"))
num2 = int(input("Введите 2ое число:"))
chastn = num1 / num2 if num2 != 0 else "infinity"
print(num1, " / ", num2, "=", chastn)
