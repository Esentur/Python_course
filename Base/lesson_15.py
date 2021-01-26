# global and local variables
def sum(x, y):
    s = float(x) + float(y)
    if isprint:
        print(s)
    else:
        return s
def sub(x,y):
    global result #keyword for use  a global variable
    result=float(x)-float(y)

result=0
isprint = False
x = input("Введите число 1: ")
y = input("Введите число 2: ")
print("Сумма равна: ", sum(x, y))
sub(x,y)
print("Разность равна: ", result)
print('---------------------------')
#exercise
def getCircleArea(r):
    global pi
    pi=pi*r**2
    return pi

pi=3.141592
r=float(input('Введите радиус окружности :'))
print(getCircleArea(r))


