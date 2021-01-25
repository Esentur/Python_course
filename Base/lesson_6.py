# строковые операции
mystr1 = "abc"
mystr2 = 'xyz'
print("concutination: ",mystr1+mystr2)
mystr1 ='''Длинная строка
на несколько
строк'''
print(mystr1)

number1 = input("Введите первое число:")
print("Вы ввели:", number1)
print("Введите второе число:")
number2 = input()
print("Вы ввели:", number2)
print("Конкатинация: ", number1+number2)

#print("Сумма введенных чисел:", int(number1)+int(number2))
print("Сумма введенных чисел:", float(number1)+float(number2))

# exercise
print("Exercise: ---------------------")
num1 = int(input("Введите 1ое число:"))
num2 = int(input("Введите 2ое число:"))
num3 = int(input("Введите 3ое число:"))
print(" Среднее арифмитическое введенных вами чисел:", num1,num2,num3,"равняется", ((num1+num2+num3)/3))
