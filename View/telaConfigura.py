from tkinter import *

def TelaConfigura(tela):

    # Cria a tela de configuração
    telaConfig = Toplevel(tela)
    telaConfig.title('CONFIGURAÇÕES')
    telaConfig.geometry('280x180+620+120')
    telaConfig['bg'] = 'gray'
    telaConfig.resizable(False,False)
    telaConfig.focus_force()
    telaConfig.grab_set()

    # Lables de porta e arduino
    lblPorta = Label(telaConfig,text='PORTA USB :',foreground='black',bg='gray',anchor=W,)
    lblPorta.place(x=30,y=30)
    lblArduino = Label(telaConfig,text='ARDUINO :',foreground='black',bg='gray',anchor=W,)
    lblArduino.place(x=30,y=70)

    # Escolhe a porta e o tipo de arduino
    listaPorta = ['COM 1','COM 2','COM 3']
    listaArduino = ['UNO','MEGA']

    clickPorta = StringVar()
    clickPorta.set('USB')

    clickArduino = StringVar()
    clickArduino.set('ARDUINO')

    porta = OptionMenu(telaConfig,clickPorta,*listaPorta)
    porta.place(x=150,y=30,width=90,height=20)
    arduino = OptionMenu(telaConfig,clickArduino,*listaArduino)
    arduino.place(x=150,y=70,width=90,height=20)

    # Botão de conexão
    btnCnt = Button(telaConfig,text='CONECTAR',command = '',foreground='white',bg='black')
    btnCnt.place(x=165,y=120)