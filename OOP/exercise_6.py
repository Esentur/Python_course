# наследование и переопределение методов. НАСЛЕДОВАНИЕ И ПОЛИМОРФИЗМ
class Auto:
    x=0
    y=0
    maxSpeed=0
    def __init__(self,x,y,maxSpeed):
        self.x=x
        self.y=y
        self.maxSpeed=maxSpeed
    def toDrive(self,x,y):
        self.x=x
        self.y=y
        print('Движение Auto в точку',x,y)
class Mercedes(Auto):
    model='Mercedes'
    haveAmgPackage =True
    def __init__(self,x,y,maxSpeed,model,haveAmgPackage):
        Auto.__init__(self,x,y,maxSpeed)
        self.model=model
        self.haveAmgPackage=haveAmgPackage

    def toDrive(self,x,y):
        print('Движение',self.model,'в точку', x,y)

auto=Auto(0,0,100)
auto.toDrive(1,1)

mercedes=Mercedes(0,0,240,'CLA 2020',True)
mercedes.toDrive(100,100)
