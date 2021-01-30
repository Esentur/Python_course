# Основные строковые функции
def isfloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


s1 = 'str_1'

print(len(s1))
print(s1[1])
print(s1[-1])
print(s1[-2])
print(s1[0:3])

s1 = 'abc\\nxyz'
s2 = r'abc\nxyz'
print(s1)
print(s2)
print('----------------------')

s1 = 'hello'
s2 = s1 * 3
print(s1)
print(s2)

print(s1.find('l'))  # find index of symbol
print(s1.find('l'), 3)  # start searching after index 3

print('593'.isdigit())
print('abconly'.isalpha())

print(s1.upper())
print(s1.lower())
print('----------------------')

print(ord('a'))
print(chr(98))

s1 = '       hello     '
print(s1)
print(s1.strip())

s1 = 'Здравствуйте, {0}. Вам {1} лет'
print(s1.format('Esentur', 23))

s1 = 'Здравствуйте, {name}. Вам {age} лет.'
print(s1.format(name='Esentur', age=23))

data=('Alex',30)
s1 = 'Здравствуйте, {0[0]}. Вам {0[1]} лет'
print(s1.format(data))

s1='int:{0:d};bin: {0:b}'
print(s1.format(5))

s1='round (150/47); {0:.4}'
print(s1.format(150/47))
print('------------------------------------')
#exercise
print('exercise')

mylist=input('Пожалуйста введите произвольную строку :\n')
for i in mylist:
    print(ord(i))

mylist=input('Пожалуйста введите строку только из цифр :\n')
try:
    if mylist.isdigit():
        print('Спасибо!')
    else:
        raise Exception('Некорректный ввод!')
except Exception as myexp:
    print(myexp)

