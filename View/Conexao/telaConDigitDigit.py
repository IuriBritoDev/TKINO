from tkinter import *
from Controller import controleBanco


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

    valAtuador = controleBanco.ControleLerDados('*',1)

    qtdSensores = len(valAtuador)

    sensor = []
    controlador = []
    
    for n in range(0,qtdSensores):

        # Se a conexão for sensor
        if (valAtuador[n][2] == '1'):
            if (valAtuador[n][3] == '1'):
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

    def CriaConexao():
        tb = 0
        interog = '?,?,?,?'
        valoresConex = [('1','1',)]
        
        voloresConexAtua = [(clickSensor.get(),clickControlador.get(),clickValSensor.get(),clickValControlador.get(),)]
        
        controleBanco.ControleCriaConexao(valoresConex)
        controleBanco.ControleCriaConexAtuadores(tb,voloresConexAtua,interog)
        
        telaCadastro.destroy()

    # Botão de conexão
    btnCnt = Button(telaCadastro,text='CONECTAR',command = CriaConexao,foreground='white',bg='black')
    btnCnt.place(x=300,y=350)