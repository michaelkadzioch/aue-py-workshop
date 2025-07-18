import tkinter
from tkinter import messagebox

def btn1_click():
    # Messagebox.art('titel', 'Ausgabetext')
    # Infobox
    msgReturnWert = messagebox.showinfo('Info', 'Button wurde geklickt')
    print(msgReturnWert)

def btn2_click():
    # Messagebox.art('titel', 'Ausgabetext')
    # Warning
    msgReturnWert = messagebox.showwarning('Warnung', 'Button wurde geklickt')
    print(msgReturnWert)


def btn3_click():
    # Messagebox.art('titel', 'Ausgabetext')
    # Error
    msgReturnWert = messagebox.showerror('Error', 'Button wurde geklickt')
    print(msgReturnWert)


def btn4_click():
    # Messagebox.art('titel', 'Ausgabetext')
    # Frage
    msgReturnWert = messagebox.askquestion('Frage', 'Ja oder Nein')
    print(msgReturnWert)


def btn5_click():
    # Messagebox.art('titel', 'Ausgabetext')
    # Frage
    msgReturnWert = messagebox.askyesno('Frage', 'Ja oder Nein')
    print(msgReturnWert)


def btn6_click():
    # Messagebox.art('titel', 'Ausgabetext')
    # Frage
    msgReturnWert = messagebox.askyesnocancel('Frage', 'Ja, Nein oder Abbruch')
    print(msgReturnWert)


def btn7_click():
    # Messagebox.art('titel', 'Ausgabetext')
    # Frage
    msgReturnWert = messagebox.askokcancel('Frage', 'Ok oder Abbruch')
    print(msgReturnWert)


def btn8_click():
    # Messagebox.art('titel', 'Ausgabetext')
    # Frage
    msgReturnWert = messagebox.askretrycancel('Frage', 'Wiederholen?')
    print(msgReturnWert)



appWindow = tkinter.Tk()
appWindow.title('GUI mit Messageboxen')
appWindow.geometry('500x400')


btn1 = tkinter.Button(appWindow, 
                       text='Info',
                       command=btn1_click)
btn1.pack(pady=10)

btn2 = tkinter.Button(appWindow, 
                       text='Warnung',
                       command=btn2_click)
btn2.pack(pady=10)

btn3 = tkinter.Button(appWindow, 
                       text='Error',
                       command=btn3_click)
btn3.pack(pady=10)

btn4 = tkinter.Button(appWindow, 
                       text='Frage askquestion',
                       command=btn4_click)
btn4.pack(pady=10)

btn5 = tkinter.Button(appWindow, 
                       text='Frage askyesno',
                       command=btn5_click)
btn5.pack(pady=10)

btn6 = tkinter.Button(appWindow, 
                       text='Frage askyesnocanel',
                       command=btn6_click)
btn6.pack(pady=10)

btn7 = tkinter.Button(appWindow, 
                       text='Frage askokcanel',
                       command=btn7_click)
btn7.pack(pady=10)

btn8 = tkinter.Button(appWindow, 
                       text='Frage askretrycancel',
                       command=btn8_click)
btn8.pack(pady=10)

appWindow.mainloop()