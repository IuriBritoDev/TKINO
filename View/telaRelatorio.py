from tkinter import *
from tkinter import ttk
from Controller import controleBanco


# Tela de relatorios em xlsx
def TelaRelatorio(tela):

    # Cria a tela de relatorios 
    telaRelatorio = Toplevel(tela)
    telaRelatorio.title('RELATORIO')
    telaRelatorio.geometry('500x500+620+120')
    telaRelatorio['bg'] = 'gray'
    telaRelatorio.resizable(False,False)
    telaRelatorio.focus_force()
    telaRelatorio.grab_set()

    listaI = controleBanco.BuscaPrimeiro(3)
    listaF = controleBanco.BuscaUltimo(3)
   
    if(listaI == None):
        
        listaDiasI = ' '
        listaDiasF = ' '
    else:
        listaDiasI = listaI
        listaDiasF = listaF

    # Lables de data
    lblDataI = Label(telaRelatorio,text='DATA DE INICIO          '+listaDiasI,foreground='black',bg='gray',anchor=W,)
    lblDataI.place(x=20,y=30)
    lblDataF = Label(telaRelatorio,text='DATA DE FIM           '+listaDiasF,foreground='black',bg='gray',anchor=W,)
    lblDataF.place(x=20,y=90)
    
    # Pega as datas que foram digitadas e retorna uma tabela com os dados dentro da data
    def PegaData():

        idInicio = controleBanco.BuscaPrimeiro(2)
        idFim = controleBanco.BuscaUltimo(2)
        dadosSeparados = controleBanco.BuscaDadosPeloId(idInicio, idFim)
      
        return dadosSeparados

    def Escreve():
        
        d = PegaData()
        if(d != None):
            controleBanco.EscreveNoExcel(d)
        telaRelatorio.destroy()

    # Botão salver em excel
    btn = Button(telaRelatorio,text='SALVAR EM EXCEL',command = Escreve,foreground='white',bg='black')
    btn.place(x=370,y=440)

    # Formata a tabela 
    tabela = ttk.Treeview(telaRelatorio)
    tabela.place(x=10,y=165,width=465,height=230)

    #ESCREVE OS DADOS NA TABELA
    def EscreveNaTabela():
    
        dadosFormat = PegaData()
        
        if(dadosFormat != None):
            for i in range(len(dadosFormat)):
                tabela.insert(parent='',index='end',id=i,text="",values=(dadosFormat[i]))

    barraDeRoalgem = Scrollbar(telaRelatorio,orient='vertical',command='')
    barraDeRoalgem.place(x=465,y=165,width=15,height=230)
    tabela.configure(yscrollcommand=barraDeRoalgem.set)

    barraDeRoalgemH = Scrollbar(telaRelatorio,orient='horizontal',command='')
    barraDeRoalgemH.place(x=10,y=394,width=470,height=15)
    tabela.configure(xscrollcommand=barraDeRoalgemH.set)

    dados = controleBanco.ControleLerDados('Nome', 1)
    qtDados = len(dados)

    teste = ()
    teste = teste + ("col0","col1","col2",)
 
    for n in range(0,qtDados):
    
        aux = str(n+3)
        teste = teste + ("col"+aux,)

    tabela['column'] = teste

    tabela.column("#0",width=0,minwidth=0)
    tabela.column('col0',width=96,anchor=W,minwidth=96)
    tabela.column('col1',width=96,anchor=W,minwidth=96)
    tabela.column('col2',width=96,anchor=W,minwidth=96)

    for i in range(0,qtDados):

        aux = str(i+3)
        tabela.column('col'+aux,width=50,anchor=W,minwidth=50)

    tabela.heading("#0",text="")
    tabela.heading("col0",text="ID",anchor=W)
    tabela.heading("col1",text="Data",anchor=W)
    tabela.heading("col2",text="Hora",anchor=W)

    for i in range(0,qtDados):

        aux2 = str(i+3)
        tabela.heading('col'+aux2,text="VAR",anchor=W)
        
    EscreveNaTabela()