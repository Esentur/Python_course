# functions or def
def printpython():
    print("Python")


printpython()


def sum(x, y):
    return x + y


def sub(x, y):
    return x - y


def summaprint(x, y, r=False):
    s = sum(x, y)
    if r:
        return s
    else:
        print(s)


def bigsum(*numbers):
    s = 0
    print(numbers)
    for n in numbers:
        s += n
    return s


def printdict(**dict):
    for key in dict:
        print(key, "=", dict[key])


def getMax(arr):
    max = arr[0]
    for n in arr:
        if n > max:
            max = n
    return max


print(sub(7, 5))
s = sum(5, 4)
print(s)

summaprint(3, 4)
print(summaprint(3, 4, True))

print(sub(y=10, x=5))

print(bigsum(1, 5, 7, 0, 1))  # * parameters

printdict(name='Alex', age=15)  # ** parameters

print("anonimous func or lambda")

lambdafunc = lambda x, y: print(x + y)
lambdafunc(5, 6)

result = (lambda x, y: x + y)(1, 3)
print(result)

print("--------------------------")
print(getMax([5, 7, 0, 12, 1]))
print(getMax([-5, -7, 1, 10, 50, 99]))

print("--------------------------")


# exercise

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

def getMaxx(list):
    maxx = list[0]
    for i in list:
        if i > maxx:
            maxx = i
    return maxx

def getAvg(*numbers):
    print(numbers)
    summa = 0
    for m in numbers:
        summa += m
    return summa / len(numbers)

print(isEven(8))
print(getMaxx([2, 4, 5, 6, 7, 88, 33]))
print(getAvg(1, 2, 3))
