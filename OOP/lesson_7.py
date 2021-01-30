# АБСТРАГИРОВАНИЕ. абстрактный класс это класс от которого можно только наследоваться НО нельзя создавать экземпляр
from abc import ABC, abstractmethod
class Shape(ABC):
    x=0
    y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def printXY(self):
        print('('+str(self.x)+'; '+str(self.y)+')')

    @abstractmethod
    def draw(self):
        pass
        # пишем только pass. т.к. делая метод абстрактным мы говорим: "Наличие - сейчас, реализация - потом"

class Circle(Shape):
    r=0
    def __init__(self,x,y,r):
        Shape.__init__(self,x,y)
        self.r=r
    def draw(self): # !обязательно! реализуем абстрактный метод
        print('Рисуем окружность (x=',self.x,';y=',self.y,';r=',self.r,';)',sep='')
class Rectangle (Shape):
    w=0
    h=0
    def __init__(self,x,y,w,h):
        Shape.__init__(self,x,y)
        self.w=w
        self.h=h
    def draw(self):
        print('Рисуем прямоугольник (x=',self.x,';y=',self.y,';w=',self.w,';h=',self.h,';)',sep='')
# s=Shape(5,7) не может т.к. есть абстр.метод в абстр.классе
# s.draw()

c=Circle(10,20,5)
c.draw()

r=Rectangle(0,0,30,50)
r.w=35
r.draw()

c.printXY()
r.printXY()