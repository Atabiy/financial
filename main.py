from tkinter import *  


root = Tk()
# Указываем фоновый цвет
root['bg'] = '#fafafa'
# Указываем название окна
root.title('Курс валют')
# Указываем размеры окна
root.geometry('300x250')
# Делаем невозможным менять размеры окна
root.resizable(width=False, height=False)

# Фрейм даты и времени
frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.15)

# Фрейм данных
frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.075, rely=0.3, relwidth=0.85, relheight=0.4)

date = Label(frame_top, text='Дата', bg='#ffb700', font='Courier 12').pack(side=LEFT, padx=25)
time = Label(frame_top, text='Время', bg='#ffb700', font='Courier 12').pack(side=RIGHT, padx=25)

title = Label(root, text='Курс обмена валют', bg='#fafafa', font='Courier 12').pack(pady=50)

buy = Label(frame_bottom, text='Покупка', bg='#ffb700', font='Courier 12').place(x=65)
sale = Label(frame_bottom, text='Продажа', bg='#ffb700', font='Courier 12').place(x=160)
USD = Label(frame_bottom, text='USD', bg='#ffb700', font='Courier 12').place(x=13, y=30)
EUR = Label(frame_bottom, text='EUR', bg='#ffb700', font='Courier 12').place(x=13, y=60)
USD_buy = Label(frame_bottom, text='90.15', bg='#ffb700', font='Courier 12').place(x=65, y=30)
USD_sale = Label(frame_bottom, text='75', bg='#ffb700', font='Courier 12').place(x=65, y=60)
EUR_buy = Label(frame_bottom, text='90.15', bg='#ffb700', font='Courier 12').place(x=160, y=30)
EUR_sale = Label(frame_bottom, text='75', bg='#ffb700', font='Courier 12').place(x=160, y=60)



root.mainloop()
