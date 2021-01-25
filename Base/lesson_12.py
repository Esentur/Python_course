# кортежи- константы т.е неизмен-й список
myTuple = tuple()
print(myTuple)
myTuple = ()
print(myTuple)

# создание кортежа из 1 элемента
myTuple = (1,)
print(myTuple)

myTuple = (1, "3", "5")
print(myTuple)
# myTuple[1]="5" Error
print(myTuple[1])

myTuple = tuple('Python')
print(myTuple)
print("----------------------")
# exercise

mList=input("Введите произвольную строку: ")
mList=tuple(mList)
for i in mList:
    print(i)
