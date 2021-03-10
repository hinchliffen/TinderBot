from tkinter import *
import tinderBot

# import tinderBot

def startBot():
    tProf = profile.get()
    tPass = password.get()
    tinderBot.startMethod(tProf, tPass)
    login.destroy()
# Creates intro GUI

login = Tk()
label = Label(login, text="TinderBot Login", font=('Times New Roman', '16'))
label2 = Label(login, text="Facebook Email:", font=('Times New Roman', '12'))
profile = Entry(login)
label3 = Label(login, text="Password:", font=('Times New Roman', '12'))
password = Entry(login)
enter = Button(login, text='Enter', command=startBot)

login.bind('<Return>', lambda event=NONE: enter.invoke())

label.pack()
label2.pack()
profile.pack()
label3.pack()
password.pack()
enter.pack()

login.title('Introduction')
login.geometry("300x300+120+120")
login.mainloop()
