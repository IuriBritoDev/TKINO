from tkinter import *
from Controller import controleBanco

def TelaAbrirProjeto(tela):

    # Cria a tela
    telaAbrir = Toplevel(tela)
    telaAbrir.title('ABRIR PROJETO')
    telaAbrir.geometry('300x250+620+120')
    telaAbrir['bg'] = 'gray'
    telaAbrir.resizable(False,False)
    telaAbrir.focus_force()
    telaAbrir.grab_set()


    # Busca projetos existentes no banco
    #dadosFormat = controleBanco.ControleMostraExistente()

    # Cria a caixa de prijetos existentes
    caixaLista = Listbox(telaAbrir)
    caixaLista.place(x=25,y=25,width=245,height=150)
    
    # Preenche a caixa com os projetos existentes
    #for item in dadosFormat:
    #    caixaLista.insert(END,item)

    barraDeRoalgem = Scrollbar(telaAbrir,orient='vertical',command=caixaLista.yview)
    barraDeRoalgem.place(x=260,y=25,width=15,height=150)
    caixaLista.configure(yscrollcommand=barraDeRoalgem.set)

    # Botão abrir projeto
    btnAbrir = Button(telaAbrir,text='ABRIR',command=lambda:controleBanco.ControleAbreProjeto(caixaLista.get(ACTIVE)),foreground='white',bg='black')
    btnAbrir.place(x=232,y=200)