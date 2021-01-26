# modules=library

# import random
# import math as m
from random import *
from math import sin, cos
import math, cmath as cm
# import calc
from calc import *

# print(random.randint(0,10))
# print(m.sin(1))
print(randint(0, 10))
print(sin(1), cos(1))
print(math.ceil(10.3), cm.log10(1000))

print('X from cal module =', x)

while True:
    print("1 -sum; 2 -sub; 3 -mult; 4 -div; 0 -exit;")
    code = input('Enter command : ')
    if code == '0':
        exit(0)
    a = float(input('First num is: '))
    b = float(input('Second num is: '))
    if code == '1':
        r = sum(a, b)
    elif code == '2':
        r = sub(a, b)
    elif code == '3':
        r = mult(a, b)
    elif code == '4':
        r = div(a, b)
    else:
        print("Error! Unknown command(")
        break
    print('Result: ', r)
