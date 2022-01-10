from tkinter import *


# Tela de conexão analogico com analogico
def TelaConAnalogAnalog(tela):

    # Cria a tela de conexão analogico com analogico
    telaCadastro = Toplevel(tela)
    telaCadastro.title('CONEXÃO ANALOGICA ANALOGICA')
    telaCadastro.geometry('400x400+620+120')
    telaCadastro['bg'] = 'gray'
    telaCadastro.resizable(False,False)
    telaCadastro.focus_force()
    telaCadastro.grab_set()

    # Lables de sensor e controlador
    lblSensor = Label(telaCadastro,text='SENSOR :',foreground='black',bg='gray',anchor=W,)
    lblSensor.place(x=20,y=30)
    lblControlador = Label(telaCadastro,text='CONTROLADOR :',foreground='black',bg='gray',anchor=W,)
    lblControlador.place(x=220,y=30)

    sensor = ['sen1','sen2','sen3']
    controlador = ['con1','con2','con3']

    clickSensor = StringVar()
    clickSensor.set('SENSOR')

    clickControlador = StringVar()
    clickControlador.set('CONTROLADOR')

    conexao = OptionMenu(telaCadastro, clickSensor,*sensor)
    conexao.place(x=20,y=70,width=130,height=20)
    arduino = OptionMenu(telaCadastro, clickControlador,*controlador)
    arduino.place(x=220,y=70,width=130,height=20)

    # Lables de sensor e controlador
    lblSensor = Label(telaCadastro,text='SENSOR :                                    ->  CONTOLADOR',foreground='black',bg='gray',anchor=W,)
    lblSensor.place(x=20,y=180)
    lblControlador = Label(telaCadastro,text='SENSOR :                                   ->  CONTOLADOR',foreground='black',bg='gray',anchor=W,)
    lblControlador.place(x=20,y=230)

    operadores = ['=','>=','<=']

    clickOperador1 = StringVar()
    clickOperador1.set('-')

    clickOperador2 = StringVar()
    clickOperador2.set('-')

    clickOperador3 = StringVar()
    clickOperador3.set('-')

    clickOperador4 = StringVar()
    clickOperador4.set('-')
    
    operasen1 = OptionMenu(telaCadastro, clickOperador1, *operadores)
    operasen1.place(x=80,y=180,width=50,height=20)
    operasen2 = OptionMenu(telaCadastro, clickOperador2, *operadores)
    operasen2.place(x=80,y=230,width=50,height=20)
    operaCon1 = OptionMenu(telaCadastro, clickOperador3, *operadores)
    operaCon1.place(x=280,y=180,width=50,height=20)
    operaCon2 = OptionMenu(telaCadastro, clickOperador4, *operadores)
    operaCon2.place(x=280,y=230,width=50,height=20)

    # Valor do sensor analogico 1
    valorSen1 = Entry(telaCadastro)
    valorSen1.place(x=140,y=180,width=30,height=20)

    # Valor do sensor analogico 2
    valorSen2 = Entry(telaCadastro)
    valorSen2.place(x=140,y=230,width=30,height=20)

    # Valor do sensor analogico 1
    valorCon1 = Entry(telaCadastro)
    valorCon1.place(x=340,y=180,width=30,height=20)

    # Valor do sensor analogico 2
    valorCon2 = Entry(telaCadastro)
    valorCon2.place(x=340,y=230,width=30,height=20)

    # Botão de conexão
    btnCnt = Button(telaCadastro,text='CONECTAR',command = '',foreground='white',bg='black')
    btnCnt.place(x=300,y=350)