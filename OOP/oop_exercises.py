print('exercises for h/w')


class Point:
    __x = 0
    __y = 0

    def getX(self):
        self.__printLog('Запрошено свойство __x')
        return self.__x

    def getY(self):
        self.__printLog('Запрошено свойство __y')
        return self.__y

    def setX(self, x):
        self.__printLog('Изменено свойство __x')
        self.__x = x

    def setY(self, y):
        self.__printLog('Изменено свойство __y')
        self.__y = y

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __printLog(self, str):
        print(str)


class Rectangle:
    luPoint = Point()
    __a = 0
    __b = 0

    def getA(self):
        self.__printLog('Запрошено свойство __a')
        return self.__a

    def getB(self):
        self.__printLog('Запрошено свойство __b')
        return self.__b

    def setA(self, a):
        self.__printLog('Изменено свойство __a')
        self.__a = a

    def setB(self, b):
        self.__printLog('Изменено свойство __b')
        self.__b = b

    def __init__(self, luPoint=Point(), a=0, b=0):
        self.luPoint = luPoint
        self.__a = a
        self.__b = b

    def __str__(self):
        return 'Прямоугольник с координатами (' + str(self.luPoint.getX()) + ';' + str(
            self.luPoint.getY()) + ') длиной - ' + str(self.__a) + ' шириной - ' + str(self.__b)

    def recArea(self):
        return self.__a * self.__b

    def recPer(self):
        return (self.__a + self.__b) * 2

    def __printLog(self, str):
        print(str)


# #2h/w - создать объект, вывести все поля, изменить и вывести поле
# rec2 = Rectangle()
# print('luPoint ={};{} a={} b={}'.format(rec2.luPoint.x,rec2.luPoint.y, rec2.a, rec2.b))
# rec2.a = 5
# print('edited a =',rec2.a)
# print('--------------------------------')
# #3h/w - создать конструктор, дать значения при вызове, вывести все поля
# rec3=Rectangle(Point(3,3),1,3)
# print('luPoint ={};{} a={} b={}'.format(rec3.luPoint.x,rec3.luPoint.y, rec3.a, rec3.b))
# print('--------------------------------')
# #4h/w -создать 3 метода __str__(),площадь, периметр
# rec4=Rectangle(Point(4,4),4,5)
# print(rec4)
# print('Area: ',rec4.recArea())
# print('Perimeter: ',rec4.recPer())
# print('--------------------------------')

# #5h/w -private поля и методы ИНКАПСУЛЯЦИЯ
p = Point(1, 1)
print(p.getX())
print(p.getY())
p.setX(2)
p.setY(2)
print(p.getX())
print(p.getY())
print('------------------------------------------------')
rec = Rectangle(p, 1, 1)
print(rec.getA())
print(rec.getB())
rec.setA(2)
rec.setB(2)
print(rec.getA())
print(rec.getB())
