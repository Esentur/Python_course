# создание окна или любых других элементов
from tkinter import *

root = Tk()
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
# root.geometry('800x600+100+50') на случай если хотим выводить в указ-й позиции

root.geometry('{0}x{1}+{2}+{3}'.format(w, h, x, y))  # выводим окно по центру любого экрана
root.mainloop()
