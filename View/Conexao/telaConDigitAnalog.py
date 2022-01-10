from tkinter import *


# Tela conexão digital com analogico
def TelaConDigAnalog(tela):

    # Cria a tela de conexão digital com analogico
    telaCadastro = Toplevel(tela)
    telaCadastro.title('CONEXÃO DIGITAL ANALOG')
    telaCadastro.geometry('400x400+620+120')
    telaCadastro['bg'] = 'gray'
    telaCadastro.resizable(False,False)
    telaCadastro.focus_force()
    telaCadastro.grab_set()

    # Lables de sensor e controlador
    lblSensor = Label(telaCadastro,text='SENSOR :',foreground='black',bg='gray',anchor=W,)
    lblSensor.place(x=40,y=30)
    lblControlador = Label(telaCadastro,text='CONTROLADOR :',foreground='black',bg='gray',anchor=W,)
    lblControlador.place(x=220,y=30)

    sensor = ['sen1','sen2','sen3']
    controlador = ['con1','con2','con3']

    clickSensor = StringVar()
    clickSensor.set('SENSOR')

    clickControlador = StringVar()
    clickControlador.set('CONTROLADOR')

    conexao = OptionMenu(telaCadastro, clickSensor,*sensor)
    conexao.place(x=40,y=70,width=130,height=20)
    arduino = OptionMenu(telaCadastro, clickControlador,*controlador)
    arduino.place(x=220,y=70,width=130,height=20)

    # Lables de sensor e controlador
    lblSensor = Label(telaCadastro,text='SENSOR :          ON            ->    CONTOLADOR     =',foreground='black',bg='gray',anchor=W,)
    lblSensor.place(x=40,y=180)
    lblControlador = Label(telaCadastro,text='SENSOR :          OFF           ->    CONTOLADOR     =',foreground='black',bg='gray',anchor=W,)
    lblControlador.place(x=40,y=230)

    # Valor do atuador com o sensor on
    valorOn = Entry(telaCadastro)
    valorOn.place(x=320,y=180,width=30,height=20)
    # Valor do atuador com o sensor on
    valorOff = Entry(telaCadastro)
    valorOff.place(x=320,y=230,width=30,height=20)
   
    # Botão de conexão
    btnCnt = Button(telaCadastro,text='CONECTAR',command = '',foreground='white',bg='black')
    btnCnt.place(x=300,y=350)