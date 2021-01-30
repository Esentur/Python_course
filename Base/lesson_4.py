x = 15
y = 20
print("x =", x)
print("y =", y)

# основные арифметческие операции

print("x+y =", x + y)
print("x-y =", x - y)
print("x*y =", x * y)
print("x/y =", x / y)
print("x%y =", x % y)  # остаток от деления
print("x//y =", x // y)  # целая часть при делении

print("x**y =", x ** y)  # возведение в степень а^b
print("2**3 =", 2 ** 3)  # возведение в степень а^b
print("(2+3*3)*2 =", (2 + 3 * 3) * 2)

# битовые операции

x = 5
y = 7
print("x =", x, "bin(x) =", bin(x))
print("x =", x, "hex(x) =", hex(x))
print("hex(20) =", hex(20))
print("oct(10) =", oct(10))

print("---------------------------")
print("x =", x, "bin(x) =", bin(x))
print("y =", x, "bin(y) =", bin(y))
print("x|y =", bin(x | y))  # битовое ИЛИ. ставит 1 если хоть один из них равна 1
print("x&y =", bin(x & y))  # битовое И. ставит 1 если оба равны 1
print("x^y =", bin(x ^ y))  # битовое Исключающее ИЛИ. ставит 1 если есть разница в операндах. иначе 0
print("~x =",bin(~x))  # битовое Отицание. меняет 0 на 1 . 1 на 0. При выводе. 1 означает "-". 0 означает "+"впереди числа
print(x)
print("x<<1 =", bin(x << 1))  # сместить на 1 число влево = *2
print("x>>1 =", bin(x >> 1))  # сместить на 1 число налево = /2

# exercise
print("Exercise: ---------------------")
a = 7
b = 15
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print('a//b',a // b)
print(a ** b)
print((((15 * 10 - 20) / 2) + 14 * 10 + (-45)))
z = 25
print("bin(z) =", bin(z))
