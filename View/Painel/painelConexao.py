from tkinter import *
from Controller import controleTelas, controleBanco


def PainelConexao(frame, tela):

    valSensores = []
    nnomeSensores = []
    col = '*'
    
    def clear_frame():
        for widgets in frame.winfo_children():
            widgets.destroy()
    clear_frame()
    
    if (controleBanco.ControlePegaProjetoAtual() != ' '):
        valSensores = controleBanco.ControleLerDados(col,4)
        if (valSensores == []):
            valSensores = [(1, '-', '-')]
        
    valX = 100
    valY =  100
    
    qtdSernsoes = len(valSensores)
    if(qtdSernsoes != 0):
        if(valSensores[0][1]!= '-'):
            for n in range(0,qtdSernsoes):
                if (n == 4):
                    valY = 400
                    valX = 100 
                
                variavel_1 = Label(frame,text = 'SENSOR'+ '  ' + valSensores[n][1] + '\n'+'CONTROLADOR ' + valSensores[n][2] + ' \n\n\n\n' ,foreground='black',anchor=N)
                variavel_1.place(x=valX,y=valY,width=200,height=200)
                
                #btn = Button(frame,text='EDITAR',foreground='white',bg='black',command=lambda:controleTelas.AbreTelaCadastro(tela))
                #btn.place(x=valX+140,y=valY+165)
                valX+=300