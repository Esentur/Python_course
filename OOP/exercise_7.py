# АБСТРАГИРОВАНИЕ. закрепление
from abc import ABC,abstractmethod
class Auto(ABC):
    x=0
    y=0
    maxSpeed=0
    def __init__(self,x,y,maxSpeed):
        self.x=x
        self.y=y
        self.maxSpeed=maxSpeed
    @abstractmethod
    def toDrive(self,x,y):
        pass
class Toyota(Auto):
    model='Toyota'
    package4x4 =True
    def __init__(self,x,y,maxSpeed,model,package4x4):
        Auto.__init__(self,x,y,maxSpeed)
        self.model=model
        self.package4x4=package4x4

    def toDrive(self,x,y):
        self.x=x
        self.y=y
        print('Движение',self.model,'в точку', x,y)


caldina=Toyota(0,0,240,'Toyota Caldina',True)
caldina.toDrive(100,100)
print(caldina.x)