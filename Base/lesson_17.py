#exception
try:
    a = float('abc')
except ValueError:
    print('Невозможно привести к числу!')

while False:
    a = input('Enter positive num: ')
    try:
        a = float(a)
        if a <= 0:
            raise Exception('Число не положительное!')
    except ValueError:
        print('Невозможно привести к числу!')
    except Exception as exp:
        print(exp)
    else:
        print('Спасибо за корректный ввод!')
    finally:
        print('В любом случае работает finally')
print('-----------------------------')
#exercise

try:
    print('Enter two nums for division: ')
    num1 = int(input('num1: '))
    num2 = int(input('num2: '))
    result = num1 / num2
    print(num1, '/',num2, '=', result)
except ZeroDivisionError:
    print('Бесконечность')
