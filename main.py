root = Tk()
# Указываем фоновый цвет
root['bg'] = '#fafafa'
# Указываем название окна
root.title('Погодное приложение')
# Указываем размеры окна
root.geometry('300x250')
# Делаем невозможным менять размеры окна
root.resizable(width=False, height=False)

# Создаем фрейм (область для размещения других объектов)
# Указываем к какому окну он принадлежит, какой у него фон и какая обводка
frame_top = Frame(root, bg='#ffb700', bd=5)
# Также указываем его расположение
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

# Все то-же самое, но для второго фрейма
frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.11, rely=0.55, relwidth=0.8, relheight=0.1)

# Создаем текстовое поле для получения данных от пользователя
cityField = Entry(frame_top, bg='white', font=30)
cityField.pack() # Размещение этого объекта, всегда нужно прописывать

# Создаем кнопку и при нажатии будет срабатывать метод "get_weather"
btn = Button(frame_top, text='Посмотреть погоду')
btn.pack()

# Создаем текстовую надпись, в которую будет выводиться информация о погоде
info = Label(frame_bottom, text='Погодная информация', bg='#ffb700', font=40)
info.pack()

# Запускаем постоянный цикл, чтобы программа работала
root.mainloop()
