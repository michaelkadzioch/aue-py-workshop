import tkinter


def changeTextDirect():
    label1.config(text='Hier ist jetzt ein neuer Text.')

def changeTextIndirect():
    label2_output.set('Hier wird jetzt eine neue Textvariable angezeigt.')


appWindow = tkinter.Tk()
appWindow.title('Meine erste GUI')
appWindow.geometry('500x400')



label1 = tkinter.Label(appWindow, 
                       text='Hier ist ein Label mit etwas Text.',
                       font=36)
label1.pack(pady=10)

btn1 = tkinter.Button(appWindow, 
                       text='Text ändern',
                       command=changeTextDirect)
btn1.pack(pady=10)



label2_output = tkinter.StringVar()
label2_output.set('Hier wird eine Textvariable angezeigt.')

label2 = tkinter.Label(appWindow, 
                       textvariable=label2_output,
                       font=36)

label2.pack(pady=10)

btn2 = tkinter.Button(appWindow, 
                       text='Variable ändern',
                       command=changeTextIndirect)
btn2.pack(pady=10)


appWindow.mainloop()