import tkinter


def macheEineAusgabe():
    print('Ein Button wurde geklickt!')

def btnAppClose_click():
    appWindow.destroy()


# Create a window
appWindow = tkinter.Tk()
appWindow.title('Meine erste GUI')
appWindow.geometry('500x400')

# Create a Button
btn = tkinter.Button(appWindow, 
                        text='Das ist ein Button',
                        command=macheEineAusgabe)
btn['height'] = 3
btn['width'] = 20
btn['bg'] = '#ff0000'
btn['fg'] = '#ffffff'
btn.pack()
# btn.place(x=200, y=300)

# Create a Close Button
btnAppClose = tkinter.Button(appWindow, 
                            text='Schließen',
                            command=btnAppClose_click)
btnAppClose.pack()
# btnAppClose.place(x=200, y=340)

# Window in Endlosschleife laufen lassen
appWindow.mainloop()