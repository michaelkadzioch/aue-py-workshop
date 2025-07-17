import tkinter

def btnAppClose_click():
    appWindow.destroy()

def btn1_click():
    text = entrybox1.get()
    print(text)
    auswahl = radiovar.get()    
    print('Auswahl:', auswahl)


# Create a window
appWindow = tkinter.Tk()
appWindow.title('Meine erste GUI')
appWindow.geometry('500x400')


# Create a Label
label1 = tkinter.Label(appWindow, text='Hier ist ein Label mit etwas Text.')
label1.pack()

# Create a Button
btn1 = tkinter.Button(appWindow, text='Das ist ein Button', command=btn1_click)
btn1.pack()

# Create an Entrybox
entrybox1 = tkinter.Entry(appWindow)
entrybox1.pack()


# Radiobuttons
radiovar = tkinter.StringVar()
radiovar.set('Option 1 gewählt')

radio1 = tkinter.Radiobutton(appWindow, text='Option 1', variable=radiovar, value='Option 1 gewählt')
radio1.pack()
radio2 = tkinter.Radiobutton(appWindow, text='Option 2', variable=radiovar, value='Option 2 gewählt')
radio2.pack()
radio3 = tkinter.Radiobutton(appWindow, text='Option 3', variable=radiovar, value='Option 3 gewählt')
radio3.pack()


# Checkbutton
cbvar = tkinter.BooleanVar()
cbvar.set(False)

cbox1 = tkinter.Checkbutton(appWindow, text='Checkbox 1', variable=cbvar)
cbox1.pack()


# Combobox
comboboxVar = tkinter.StringVar()
comboboxVar.set('Option 1')

combobox1 = tkinter.OptionMenu(appWindow, 
                               comboboxVar, 
                               'Option 1', 'Option 2', 'Option 3')

combobox1.pack()


# Window in Endlosschleife laufen lassen
appWindow.mainloop()