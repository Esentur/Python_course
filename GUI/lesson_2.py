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
label=Label(root,text='Моя текстовая метка', font='Tahoma 18',bg='#ff0000',fg='green' )
label.pack()
#exercise new TextField
randNum=randint(1,1000)
label1=Label(root,text=randNum, font='Calibri 10', bg='#000000',fg='red')
label1.pack()
root.mainloop()

