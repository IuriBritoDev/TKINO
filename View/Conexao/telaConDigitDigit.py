from tkinter import *


# Tela conexão digital com degital
def TelaConDigDig(tela):

    # Cria a tela de conexão digital com degital
    telaCadastro = Toplevel(tela)
    telaCadastro.title('CONEXÃO DIGITAL DIGITAL')
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
    lblSensor = Label(telaCadastro,text='SENSOR :                              ->',foreground='black',bg='gray',anchor=W,)
    lblSensor.place(x=40,y=150)
    lblControlador = Label(telaCadastro,text='CONTROLADOR :',foreground='black',bg='gray',anchor=W,)
    lblControlador.place(x=220,y=150)

    valSensor = ['OFF','ON']
    valControlador = ['OFF','ON']

    clickValSensor = StringVar()
    clickValSensor.set('-')

    clickValControlador = StringVar()
    clickValControlador.set('-')

    sensorVal = OptionMenu(telaCadastro, clickValSensor,*valSensor)
    sensorVal.place(x=100,y=150,width=60,height=20)
    controladorVal = OptionMenu(telaCadastro, clickValControlador,*valControlador)
    controladorVal.place(x=320,y=150,width=60,height=20)

    # Botão de conexão
    btnCnt = Button(telaCadastro,text='CONECTAR',command = '',foreground='white',bg='black')
    btnCnt.place(x=300,y=350)