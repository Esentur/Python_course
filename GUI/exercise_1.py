from tkinter import *
root=Tk()
root.title('Exercise 1')
root.resizable(True,True)

w=1000
h=500
uw=root.winfo_screenwidth()
uh=root.winfo_screenmmheight()
# x=0;y=0 чтобы расположить окно в левом верхнем углу
x=uw-w;y=0 # чтобы расположить окно в правом верхнем углу

root.geometry('{0}x{1}+{2}+{3}'.format(w,h,x,y))
root.mainloop()
