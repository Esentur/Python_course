def readcommand(address):
    handler = open(address, 'r')
    print(handler.read())
    handler.close()


def copycommand(address):
    from_= open(address, 'r')
    text = from_.read()
    to_ = open('files/copy.txt', 'a')
    to_.write('copied text :\n')
    to_.write(text)
    to_.write('\n')
    to_.close()
    from_.close()


comand = input('Available commands :\n1 - to read\n2 - to copy \n')
if comand == '1':
    address = input('Напишите путь к файлу, содержимое которого Вы хотите посмотреть :')
    readcommand(address)
elif comand == '2':
    address = input('Напишите путь к файлу, который Вы хотите скопировать :')
    copycommand(address)
else:
    print('Неизвестная команда')
