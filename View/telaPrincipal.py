from tkinter import * 
from tkinter import ttk
from Controller import controleTelas, controleCriaTelas, controleBanco


# Tela principal do projeto
def TelaPrincipal():
    
    # Cria tela principal
    root = controleCriaTelas.CriaTela('TKINO','300x300','gray')
    root = root.parametrosTela()

    valorLargura = root.winfo_screenwidth()
    valorComprimento = root.winfo_screenheight()
    root.geometry('%dx%d+0+0' % (valorLargura-20,valorComprimento-100))

    # Cria frame para dividir a tela
    framePrincipal = Frame(root)
    framePrincipal.place(relx=0,rely=0,relwidth=1,relheight=1)

    style = ttk.Style(root)
    style.configure('lefttab.TNotebook', tabposition='wn')
    style.configure('TNotebook.Tab', font=('URW Gothic L','20','bold') )
    
    abas = ttk.Notebook(framePrincipal, style='lefttab.TNotebook')
    aba1 = Frame(abas,bg='gray')
    aba2 = Frame(abas,bg='gray')
    aba3 = Frame(abas,bg='gray')
    
    abas.add(aba1,text=f'{"SENSORES":^23s}')
    abas.add(aba2,text=f'{"CONTROLADORES":^15s}')
    abas.add(aba3,text=f'{"CONEXÃO":^23s}')
    
    abas.place(relx=0,rely=0.1,relwidth=1,relheight=1)

    def VeProjeto():

        pjtAtual = controleBanco.ControlePegaProjetoAtual()

        size = len(pjtAtual)
        nomeProjetoAtual = pjtAtual[:size - 3]
        
        variavel1 = Label(root,text='PROJETO:  ' + nomeProjetoAtual,foreground='black',anchor=N,width=8,font=20)
        variavel1.place(x=10,y=30,width=200,height=30)
      
        if (pjtAtual == ' '):
        
            sistema.entryconfig("RELATORIO", state="disabled") 
            sistema.entryconfig("CONFIGURAÇÕES", state="disabled") 
            atuadores.entryconfig("CADASTRO", state="disabled")
            atuadores.entryconfig("CONEXÃO", state="disabled")
        else:
            
            sistema.entryconfig("RELATORIO", state="normal") 
            sistema.entryconfig("CONFIGURAÇÕES", state="normal") 
            atuadores.entryconfig("CADASTRO", state="normal")
            atuadores.entryconfig("CONEXÃO", state="normal")

    def Reload():
    
        # Mostra os sensores
        controleTelas.AbreFrameSensores(aba1)
        # Mostra os controladores
        controleTelas.AbreFrameControladores(aba2,root)
        # Mostra as conexões
        controleTelas.AbreFrameConexao(aba3,root)
        
        VeProjeto()
        root.after(4000,Reload)

    # Cria a barra de menus
    menubar = Menu(root)
    arquivo = Menu(menubar, tearoff=0)
    sistema = Menu(menubar, tearoff=0)
    atuadores = Menu(menubar, tearoff=0)

    arquivo.add_command(label="NOVO",command=lambda:controleTelas.AbreTelaNovoProjeto(root))
    arquivo.add_command(label="ABRIR" , command=lambda:controleTelas.AbreTelaAbrirProjeto(root))
    arquivo.add_command(label="SAIR" , command=root.quit)

    sistema.add_command(label="RELATORIO",command=lambda:controleTelas.AbreTelaRelatorio(root))
    sistema.add_command(label="CONFIGURAÇÕES",command=lambda:controleTelas.AbreTelaConfigura(root))
    
    atuadores.add_command(label="CADASTRO",command=lambda:controleTelas.AbreTelaCadastro(root))
    atuadores.add_command(label="CONEXÃO",command=lambda:controleTelas.AbreTelaConexao(root))

    menubar.add_cascade(label="ARQUIVO", menu=arquivo)
    menubar.add_cascade(label="SISTEMA", menu=sistema)
    menubar.add_cascade(label="ATUADORES", menu=atuadores)
    
    root.config(menu=menubar)

    Reload()
    root.mainloop()