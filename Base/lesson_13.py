# словари Map, HeshMap или ассоциативные массивы
# key-value

mydict = dict()
print(mydict)
mydict = {}
print(mydict)

mydict = {'Name': 'John', 'Age': 35}
print(mydict)

mydict = dict(Name='Esen', Age=35, isMale=True)
print(mydict)

print(mydict['Age'])
print("--------------------------")

for key in mydict:
    print(key, '=', mydict[key])

mytuple = ('Name', 'Age', 'isMale')
for key in mytuple:
    print(key, '=', mydict[key])
print("--------------------------")

mydict = {i * 2: i for i in range(1, 10)}
print(mydict[2])
mydict = {str(i * 2): i for i in range(1, 10)}
print(mydict)
print("--------------------------")
# exercise

mymap = {'Name': 'Без имени', 'Age': -1}
mymap = dict(Name='empty', Age=-1)
print(mymap)
mymap['Name'] = input("Введите имя :")
mymap['Age'] = input("Введите возраст :")
for key in mymap:
    print(key, '---', mymap[key])
