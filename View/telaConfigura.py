from tkinter import *
from Controller import controleUSB, controleBanco, controleTelas


# Tela de configurações de Arduino e USP
def TelaConfigura(tela):

    # Cria a tela de configuração
    telaConfig = Toplevel(tela)
    telaConfig.title('CONFIGURAÇÕES')
    telaConfig.geometry('320x180+620+120')
    telaConfig['bg'] = 'gray'
    telaConfig.resizable(False,False)
    telaConfig.focus_force()
    telaConfig.grab_set()

    # Lables de porta e arduino
    lblPorta = Label(telaConfig,text='PORTA USB ARDUINO :',foreground='black',bg='gray',anchor=W,)
    lblPorta.place(x=30,y=30)
    

    # Escolhe a porta e o tipo de arduino
    listaPorta = []
    listaArduino = []
     
    portas = controleUSB.BuscaPortas() 
    qtdConexoes = len(portas)

    for n in range(0,qtdConexoes):

        port = portas[n]
        strPort = str(port)
        listaPorta.append(strPort)

    clickPorta = StringVar()
    clickPorta.set('USB')

    porta = OptionMenu(telaConfig,clickPorta,*listaPorta)
    porta.place(x=30,y=70,width=250,height=20)

    def Conecta():
        tb = 5
        interog = '?'
        teste = 'valor'

        strPort = clickPorta.get()
        commPort = strPort[0:4]
    
        valoresPorta = [(commPort,)]
        controleUSB.ConectaPortaUSB(commPort)
        controleBanco.ControleEscreveNaTabela(valoresPorta, interog)
        controleTelas.AbrePopUp(tela,'Conexão feita')
        telaConfig.destroy()

    # Botão de conexão
    btnCnt = Button(telaConfig,text='CONECTAR',command = Conecta,foreground='white',bg='black')
    btnCnt.place(x=210,y=120)