from tkinter import *
from Controller import controleBanco


global nomeNovo

# Tela para criar novos projetos
def TelaNovoProjeto(tela):

    # Cria a tela de novo projeto
    telaNovo = Toplevel(tela)
    telaNovo.title('NOVO PROJETO')
    telaNovo.geometry('260x150+620+220')
    telaNovo['bg'] = 'gray'
    telaNovo.resizable(False,False)
    telaNovo.focus_force()
    telaNovo.grab_set()

    txt = Label(telaNovo,text='NOME:',foreground='black',bg='gray',anchor=W,)
    txt.place(x=35,y=40)

    # Nome do novo projeto
    nomeNovo = Entry(telaNovo)
    nomeNovo.place(x=85,y=40)

    # Pega o nome do banco
    def pegaNome():
        nome = nomeNovo.get()
        controleBanco.ControleCriaBanco(nome)
        telaNovo.destroy()
        
    # Cria novo projeto
    btnCriar = Button(telaNovo,text='CRIAR',command = pegaNome,foreground='white',bg='black')
    btnCriar.place(x=165,y=90)