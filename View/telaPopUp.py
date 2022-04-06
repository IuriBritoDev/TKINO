from tkinter import *

def TelaPopUp(tela, msg):

    # Cria a tela de popup
    telaPopUp = Toplevel(tela)
    telaPopUp.title('PopUP')
    telaPopUp.geometry('280x120+620+120')
    telaPopUp['bg'] = 'white'
    telaPopUp.resizable(False,False)
    telaPopUp.focus_force()
    telaPopUp.grab_set()

    # Mensagem do PopUp
    txt = Label(telaPopUp, text=msg, foreground='black', bg='white', anchor=N,)
    txt.place(x=40, y=20)

    def Fecha():
        telaPopUp.destroy()

    # Fecha o PopUp
    btnOk = Button(telaPopUp, text='OK',command = Fecha, foreground='white', bg='black')
    btnOk.place(x=120, y=60)