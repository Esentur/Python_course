# Логические операции

b1 = True
b2 = False
print("b1 =", b1)
print("b2 =", b2)
print("b1 or b2", b1 or b2)
print("b1 and b2", b1 and b2)
print("not b1", not b1)  # отрицание логическое
print("b1!=b2", b1 != b2)  # исключающее ИЛИ
print("b1==b2", b1 == b2)  # проверка на равенство

print("------------------------------------")

x = 5
y = 7
print("x =", x)
print("y =", y)
print("x>y =", x > y)
print("x<y =", x < y)
print("x>=y =", x >= y)
print("x<=y =", x <= y)

print("x and b1 or (x>10) =", x and b1 or (x > 10))
print("x>10 or y<7 =", x > 10 or y < 7)
print("x>10 or y<=7 =", x > 10 or y <= 7)

# exercise
print("Exercise: ---------------------")
a=10
b=11
print(a==10 and(b==11 or( a>15 and a==10 or a==b)and a==10 or a==10 != False))
print(True and (True or (False and True or False) and True or True != False))
print(15 > 20 or (5 < 7 and 8 > 12 or 12 >= 12 and 15 < 18))
