#Files
handler =open('a.txt','w')
# 1 -parameter
# r открой и читай сущ-й файл
# w открой и создай новый для записи
# a открой и редак-й сущействующий не стирая содержимое
# x просто открой для записи существующий иначе ошибка
# 2 -parameter
#  rt -read text
#  rb -read bin
handler.write('abc 123\n090\n')
handler.close()

handler=open('a.txt','r')
print(handler.read(2))
print(handler.read())

handler.seek(0) #сменить указатель читателя
print(handler.read())

handler.seek(0)
for line in handler:
    print(line)

handler.close()
print('---------------')
file='b.txt'
while True:
    print('1 - to write, 2 - to read, 0 - to exit')
    inp=input('Введите команду :')
    if inp=='0':
        exit(0)
    elif inp=='1':
        text=input('Введите строку для запси :')
        handler=open(file,'w')
        handler.write(text)
        handler.close()
    elif inp=='2':
        try:
            handler=open(file,'r')
            print(handler.read())
            handler.close()
        except FileNotFoundError:
            print('Файла еще не существует')
    else:
        print('Неизвестная команда')