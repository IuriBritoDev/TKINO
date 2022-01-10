from tkinter import *

def TelaEditarControle(tela, controle):

    # Cria a tela de configuração
    telaEditar = Toplevel(tela)
    telaEditar.title('EDITA CONTROLE')
    telaEditar.geometry('280x180+620+120')
    telaEditar['bg'] = 'gray'
    telaEditar.resizable(False,False)
    telaEditar.focus_force()
    telaEditar.grab_set()

    # Lables de porta e arduino
    lblPorta = Label(telaEditar,text='VALOR CONTROLADOR',foreground='black',bg='gray',anchor=W,)
    lblPorta.place(x=50,y=20)
    
    slide = Scale(telaEditar,from_=10,to=90,orient=HORIZONTAL)
    slide.place(x=95,y=70,width=100,height=50)

    # Botão de conexão
    btnCnt = Button(telaEditar,text='SALVAR',command = '',foreground='white',bg='black')
    btnCnt.place(x=210,y=140)