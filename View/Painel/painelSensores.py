from tkinter import *
from Controller import controleBanco, controleSerial


def PainelSensores(frame):

    valSensores = []
    nnomeSensores = []

    col = '*'
    m = 0

    valX = 100
    valY =  100
    
    def clear_frame():
        for widgets in frame.winfo_children():
            widgets.destroy()

    clear_frame()

    pjtAtual = controleBanco.ControlePegaProjetoAtual()

    if (pjtAtual != ' '):

        valSensores = controleBanco.ControleLerDados(col,1)
        ultimosDados = controleBanco.ControlebuscaUltimosDados(3)

    qtdSensores = len(valSensores)
    
    for n in range(0,qtdSensores):
        
        if (m == 5):

            valY = 300
            valX = 100 
        if (valSensores[n][2] == '1'):

            if(ultimosDados == []):
                variavel1 = Label(frame,text=valSensores[n][1]+'\n\n\n',foreground='black',anchor=N,width=8)
                variavel1.place(x=valX,y=valY,width=100,height=100)

            elif(ultimosDados[0][n+3] == None):
                variavel1 = Label(frame,text=valSensores[n][1]+'\n\n\n',foreground='black',anchor=N,width=8)
                variavel1.place(x=valX,y=valY,width=100,height=100)

            else:
                variavel1 = Label(frame,text=valSensores[n][1]+'\n\n\n'+ultimosDados[0][n+3],foreground='black',anchor=N,width=8)
                variavel1.place(x=valX,y=valY,width=100,height=100)
            m+=1
            valX+=200
    

    
        
        