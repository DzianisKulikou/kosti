from tkinter import *
import random
import time


def bros():
    x = random.choice(['1.png', '2.png', '3.png', '4.png', '5.png', '6.png'])
    return x


def img(evant):
    global b1, b2, b3, b4, b5
    for i in range(random.randint(2, 13)):  # случайный выбор целых чисел в данном диапазоне
        b1 = PhotoImage(file=(bros()))
        b2 = PhotoImage(file=(bros()))
        b3 = PhotoImage(file=(bros()))
        b4 = PhotoImage(file=(bros()))
        b5 = PhotoImage(file=(bros()))
        lab1['image'] = b1
        lab2['image'] = b2
        lab3['image'] = b3
        lab4['image'] = b4
        lab5['image'] = b5
        t.update()
        time.sleep(random.choice([0.10, 0.12, 0.14, 0.16, 0.18, 0.20]))


t = Tk()
t.geometry('800x600')  # Размеры окна
t.title('Бросай кости!')  # Надпись сверху окна
t.resizable(height=False, width=False)  # блокирует изменение размеров окна
t.iconphoto(True, PhotoImage(file='ikon1.png'))  # Иконка
font = PhotoImage(file='fon2.png')  # Картинка фона
Label(t, image=font).pack()  # Размещение кубиков поверх фона
lab1 = Label(t)
lab1.place(relx=0.2, rely=0.3, anchor=CENTER)  # Расположение меток на окне
lab2 = Label(t)
lab2.place(relx=0.5, rely=0.3, anchor=CENTER)  # Расположение меток на окне
lab3 = Label(t)
lab3.place(relx=0.8, rely=0.3, anchor=CENTER)  # Расположение меток на окне
lab4 = Label(t)
lab4.place(relx=0.3, rely=0.7, anchor=CENTER)  # Расположение меток на окне
lab5 = Label(t)
lab5.place(relx=0.7, rely=0.7, anchor=CENTER)  # Расположение меток на окне
t.bind('<1>', img)
img('evant')
t.mainloop()


# pyinstaller -w kosti.py в командной строке, чтоб создать папку с игрой
# cd команда в командной строке для выбора папки