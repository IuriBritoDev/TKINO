from tkinter import *
from Controller import controleTelas
from Controller import controleBanco


def PainelControladores(frame):

    valControladores = []
    nomeControladores = []
    col = '*'

    def clear_frame():
        for widgets in frame.winfo_children():
            widgets.destroy()
    clear_frame()
    
    if (controleBanco.ControlePegaProjetoAtual() != ' '):
        valControladores = controleBanco.ControleLerDados(col,1)

    valX = 100
    valY =  100
    m = 0

    qtdSensores = len(valControladores)

    for n in range(0,qtdSensores):
        if (m == 4):
            valY = 400
            valX = 100 
        if (valControladores[n][2] == '2'):
            m+=1
            variavel_1 = Label(frame,text = valControladores[n][1],foreground='black',anchor=N)
            variavel_1.place(x=valX,y=valY,width=200,height=200)

            btn = Button(frame,text='EDITAR',foreground='white',bg='black',command=lambda:controleTelas.AbreTelaConAnAn(frame))
            btn.place(x=valX+140,y=valY+165)
            valX+=300

        