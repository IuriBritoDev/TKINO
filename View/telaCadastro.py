from tkinter import *


# Tela de cadastro de atuadores
def TelaCadastro(tela):

    # Declara variaveis
    global val1 
    global val2 

    # Cria a tela cadastro
    telaCadastro = Toplevel(tela)
    telaCadastro.title('CADASTRO')
    telaCadastro.geometry('280x240+620+120')
    telaCadastro['bg'] = 'gray'
    telaCadastro.resizable(False,False)
    telaCadastro.focus_force()
    telaCadastro.grab_set()

    # Atribui variaveis
    val1 = IntVar()
    val2 = IntVar()

    # Nome do sensor ou controlador
    nome = Label(telaCadastro,text='NOME :',foreground='black',bg='gray',anchor=W,)
    nome.place(x=10,y=20)

    nomeVar = Entry(telaCadastro)
    nomeVar.place(x=60,y=20)

    # Sensor ou controlador
    txt = Label(telaCadastro,text='TIPO :',foreground='black',bg='gray',anchor=W,)
    txt.place(x=10,y=70)

    r1 = Radiobutton(telaCadastro,text = 'SENSOR',variable = val1,value = 1)
    r1.place(x=60,y=70,width=80)
    r2 = Radiobutton(telaCadastro,text = 'CONTROLADOR',variable = val1,value = 2)
    r2.place(x=160,y=70,width=110)

    # Tipo de atuador
    txt = Label(telaCadastro,text='TIPO :',foreground='black',bg='gray',anchor=W,)
    txt.place(x=10,y=120)

    r1 = Radiobutton(telaCadastro,text = 'DIGITAL',variable = val2,value = 1)
    r1.place(x=60,y=120,width=80)
    r2 = Radiobutton(telaCadastro,text = 'ANALOGICO',variable = val2,value = 2)
    r2.place(x=160,y=120,width=110)

    # Botão cria atuador
    btn = Button(telaCadastro,text='CRIAR',foreground='white',bg='black',command = '')
    btn.place(x=215,y=180)