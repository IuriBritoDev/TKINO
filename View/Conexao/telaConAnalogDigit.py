from tkinter import *
from Controller import controleBanco


# Tela de conexão analogico com digital
def TelaConAnalogDig(tela):

    # Cria a tela de conexão analogico com digital
    telaCadastro = Toplevel(tela)
    telaCadastro.title('CONEXÃO ANALOG DIGITAL')
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

    valAtuador = controleBanco.ControleLerDados('*',1)

    qtdSensores = len(valAtuador)

    sensor = []
    controlador = []
    
    for n in range(0,qtdSensores):

        # Se a conexão for sensor
        if (valAtuador[n][2] == '1'):
            if (valAtuador[n][3] == '2'):
                sensor.append(valAtuador[n][1])

        # Se a conexão for controlador
        if (valAtuador[n][2] == '2'):
            if (valAtuador[n][3] == '1'):
                controlador.append(valAtuador[n][1])

    clickSensor = StringVar()
    clickSensor.set('SENSOR')

    clickControlador = StringVar()
    clickControlador.set('CONTROLADOR')

    conexao = OptionMenu(telaCadastro, clickSensor,*sensor)
    conexao.place(x=40,y=70,width=130,height=20)
    arduino = OptionMenu(telaCadastro, clickControlador,*controlador)
    arduino.place(x=220,y=70,width=130,height=20)

    # Lables de sensor e controlador
    lblSensor = Label(telaCadastro,text='SENSOR :                                      ->    CONTOLADOR   ON',foreground='black',bg='gray',anchor=W,)
    lblSensor.place(x=40,y=180)
    lblControlador = Label(telaCadastro,text='SENSOR :                                     ->    CONTOLADOR    OFF',foreground='black',bg='gray',anchor=W,)
    lblControlador.place(x=40,y=230)

    operador = ['=','>','<','>=','<=']

    clickSensorOn = StringVar()
    clickSensorOn.set('-')

    clickSensorOff = StringVar()
    clickSensorOff.set('-')
    

    conexao = OptionMenu(telaCadastro, clickSensorOn, *operador)
    conexao.place(x=100,y=180,width=50,height=20)
    arduino = OptionMenu(telaCadastro, clickSensorOff, *operador)
    arduino.place(x=100,y=230,width=50,height=20)

    # Valor do sensor com o controlador on
    valorOn = Entry(telaCadastro)
    valorOn.place(x=160,y=180,width=30,height=20)

    # Valor do sensor com o controlador off
    valorOff = Entry(telaCadastro)
    valorOff.place(x=160,y=230,width=30,height=20)

    def CriaConexao():

        tb = 1
        interog = '?,?,?,?,?,?'
        valoresConex = [('2','1',)]
        voloresConexAtua = [(clickSensor.get(),clickControlador.get(),clickSensorOn.get(),clickSensorOff.get(),valorOn.get(),valorOff.get(),)]
        
        controleBanco.ControleCriaConexao(valoresConex)
        controleBanco.ControleCriaConexAtuadores(tb,voloresConexAtua,interog)
        
        telaCadastro.destroy()

    # Botão de conexão
    btnCnt = Button(telaCadastro,text='CONECTAR',command = CriaConexao,foreground='white',bg='black')
    btnCnt.place(x=300,y=350)