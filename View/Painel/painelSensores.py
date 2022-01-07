from tkinter import *
from Controller import controleBanco


def PainelSensores(frame):

    valSensores = []
    nnomeSensores = []

    col = '*'
    nSen = 0 
    valX = 100
    valY =  100
    m = 0

    def clear_frame():
        for widgets in frame.winfo_children():
            widgets.destroy()

    clear_frame()

    pjtAtual = controleBanco.ControlePegaProjetoAtual()
    if (pjtAtual != ' '):
        valSensores = controleBanco.ControleLerDados(col,1)

    qtdSensores = len(valSensores)
    
    for n in range(0,qtdSensores):
        
        if (m == 5):
            valY = 300
            valX = 100 
        if (valSensores[n][2] == '1'):
            m+=1
            variavel_1 = Label(frame,text=valSensores[n][1],foreground='black',anchor=N,width=8)
            variavel_1.place(x=valX,y=valY,width=100,height=100)
            valX+=200
    

    
        
        