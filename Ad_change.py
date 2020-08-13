from tkinter import *

root = Tk()

def Show():
    String = En.get()
    String = String.replace('\\', '/')
    var = StringVar(value=String)
    En.config(textvariable = var)


label = Label(root, text = '地址：', anchor = 'c',).grid(row = 0)
En = Entry(root)
En.grid(row = 0, column = 1)

Button(root, text = '确定', anchor = 'c', width = 6, height = 1, command = Show).grid(row = 2, column = 1)

root.mainloop()
