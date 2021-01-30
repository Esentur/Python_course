# создание текстовых меток
from tkinter import *
from random import *

def setWindow(root):
    root.title('Окно программы')
    root.resizable(False, False)

    w = 800
    h = 600
    # задали разрешение окна
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()
    # print(ws,wh) разрешение экрана у пользователя

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)
    # нашли центр экрана

    root.geometry('{0}x{1}+{2}+{3}'.format(w, h, x, y))  # выводим окно по центру любого экрана

root = Tk()
setWindow(root)

button=Button(root, text='My button',bg='white',fg='Green',font='Calibri 20')
button1=Button(root, text='My button1',bg='white',fg='Green',font='Calibri 25')
button.pack()
button1.pack()
#exercise
button2=Button(root, text='Exercise button',
               bg='red',
               fg='black',
               font='Arial 15',
               padx="20",             # отступ от границ до содержимого по горизонтали
               pady="10",              # отступ от границ до содержимого по вертикали
                )

button2.pack()
root.mainloop()

