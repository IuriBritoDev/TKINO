from tkinter import *
from Controller import controleTelas, controleBanco, controleSerial


def PainelControladores(frame, tela):

    valControladores = []
    nomeControladores = []
    col = '*'

    def clear_frame():
        for widgets in frame.winfo_children():
            widgets.destroy()
    clear_frame()
    
    if (controleBanco.ControlePegaProjetoAtual() != ' '):
        valControladores = controleBanco.ControleLerDados(col,1)
        # Busca no banco todos os controladores
        parametrosControle = controleBanco.ControleLerDados(col,2)
        # Busca os ultimos dados inseridos na tabela
        ultimosDados = controleBanco.ControlebuscaUltimosDados(3)

    valX = 100
    valY =  100
    m = 0

    qtdSensores = len(valControladores)

    def DefineControlador(valorC):

        if(valorC == 'ON'):
            controleSerial.Input("A")

        if(valorC == 'OFF'):
            controleSerial.Input("B")

    for n in range(0,qtdSensores):
        if (m == 4):
            valY = 400
            valX = 100 
        
        if (valControladores[n][2] == '2'):
            m+=1
            #variavel_1 = Label(frame,text = valControladores[n][1],foreground='black',anchor=N)
            #variavel_1.place(x=valX,y=valY,width=200,height=200)
            if(ultimosDados == []):
                variavel1 = Label(frame,text=valControladores[n][1]+'\n\n\n',foreground='black',anchor=N,width=8)
                variavel1.place(x=valX,y=valY,width=200,height=200)

            elif(ultimosDados[0][n+3] == None):
                variavel1 = Label(frame,text=valControladores[n][1]+'\n\n\n',foreground='black',anchor=N,width=8)
                variavel1.place(x=valX,y=valY,width=200,height=200)

            else:
                variavel1 = Label(frame,text=valControladores[n][1]+'\n\n\n'+ultimosDados[0][n+3],foreground='black',anchor=N,width=8)
                variavel1.place(x=valX,y=valY,width=200,height=200)

            if (valControladores[n][3] == '1'):

                btnLigar = Button(frame,text='LIGAR',foreground='white',bg='black',command=lambda:DefineControlador('ON'))
                btnLigar.place(x=valX+20,y=valY+165)

                btnDesligar = Button(frame,text='DESLIGAR',foreground='white',bg='black',command=lambda:DefineControlador('OFF'))
                btnDesligar.place(x=valX+120,y=valY+165)

            if (valControladores[n][3] == '2'):

                cont = valControladores[n][3]

                variavel_1 = Label(frame,text = cont,foreground='black',anchor=N)
                variavel_1.place(x=valX,y=valY,width=200,height=200)

                btn = Button(frame,text='EDITAR',foreground='white',bg='black',command=lambda:controleTelas.AbreEditorControlador(tela,cont))
                btn.place(x=valX+140,y=valY+165)
            
            valX+=300

        