from tkinter import *
from Controller import controleBanco


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
            if (valAtuador[n][3] == '2'):
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
    
    def CriaConexao():

        tb = 2
        interog = '?,?,?,?'
        valoresConex = [('1','2',)]
        voloresConexAtua = [(clickSensor.get(),clickControlador.get(),valorOn.get(),valorOff.get(),)]
        
        controleBanco.ControleCriaConexao(valoresConex)
        controleBanco.ControleCriaConexAtuadores(tb,voloresConexAtua,interog)
        
        telaCadastro.destroy()

    # Botão de conexão
    btnCnt = Button(telaCadastro,text='CONECTAR',command = CriaConexao,foreground='white',bg='black')
    btnCnt.place(x=300,y=350)