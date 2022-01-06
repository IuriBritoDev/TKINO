from tkinter import *


# Tela de conexão entre atuadores
def TelaConexao(tela):

    # Declara variaveis
    global val1 
    global val2

    # Cria a tela de conexão entre atuadores
    telaConec = Toplevel(tela)
    telaConec.title('CONEXÃO')
    telaConec.geometry('280x220+620+120')
    telaConec['bg'] = 'gray'
    telaConec.resizable(False,False)
    telaConec.focus_force()
    telaConec.grab_set()

    # Atribui variaveis
    val1 = IntVar()
    val2 = IntVar()

    # Sensor ou controlador
    txt = Label(telaConec,text='SENSOR:',foreground='black',bg='gray',anchor=W,)
    txt.place(x=30,y=20)

    r1 = Radiobutton(telaConec,text = 'DIGITAL',variable = val1,value = 1)
    r1.place(x=30,y=50,width=80)
    r2 = Radiobutton(telaConec,text = 'ANALOGICO',variable = val1,value = 2)
    r2.place(x=140,y=50,width=110)

    # Tipo de atuador
    txt = Label(telaConec,text='CONTROLADOR:',foreground='black',bg='gray',anchor=W,)
    txt.place(x=30,y=90)

    r1 = Radiobutton(telaConec,text = 'DIGITAL',variable = val2,value = 1)
    r1.place(x=30,y=120,width=80)
    r2 = Radiobutton(telaConec,text = 'ANALOGICO',variable = val2,value = 2)
    r2.place(x=140,y=120,width=110)

    # Botão cria conexão
    btn = Button(telaConec,text='CONECTAR',foreground='white',bg='black',command = '')
    btn.place(x=180,y=170)