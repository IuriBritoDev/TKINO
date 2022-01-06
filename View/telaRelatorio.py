from tkinter import *
from tkinter import ttk


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

    # Lables de data
    lblDataI = Label(telaRelatorio,text='DATA DE INICIO',foreground='black',bg='gray',anchor=W,)
    lblDataI.place(x=20,y=30)
    lblDataF = Label(telaRelatorio,text='DATA DE FIM',foreground='black',bg='gray',anchor=W,)
    lblDataF.place(x=20,y=90)

    # Caixas de datas
    listaDias = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16']
    listaMes = ['01','02','03','04','05','06','07','08','09','10','11','12']
    listaAno = ['2019','2020','2021']

    clickDiaI = StringVar()
    clickDiaI.set('DIA')

    clickMesI = StringVar()
    clickMesI.set('MES')

    clickAnoI = StringVar()
    clickAnoI.set('ANO')

    diai = OptionMenu(telaRelatorio,clickDiaI,*listaDias)
    diai.place(x=150,y=30,width=60,height=30)
    mesi = OptionMenu(telaRelatorio,clickMesI,*listaMes)
    mesi.place(x=210,y=30,width=60,height=30)
    anoi = OptionMenu(telaRelatorio,clickAnoI,*listaAno)
    anoi.place(x=270,y=30,width=100,height=30)

    # Caixa de data final
    clickDiaF = StringVar()
    clickDiaF.set('DIA')

    clickMesF = StringVar()
    clickMesF.set('MES')

    clickAnoF = StringVar()
    clickAnoF.set('ANO')

    diaf = OptionMenu(telaRelatorio,clickDiaF,*listaDias)
    diaf.place(x=150,y=90,width=60,height=30)
    mesf = OptionMenu(telaRelatorio,clickMesF,*listaMes)
    mesf.place(x=210,y=90,width=60,height=30)
    anof = OptionMenu(telaRelatorio,clickAnoF,*listaAno)
    anof.place(x=270,y=90,width=100,height=30)

    # Botão buscar 
    btn = Button(telaRelatorio,text='BUSCAR',command = '',foreground='white',bg='black')
    btn.place(x=420,y=94)
    
    # Botão salver em excel
    btn = Button(telaRelatorio,text='SALVAR EM EXCEL',command = '',foreground='white',bg='black')
    btn.place(x=370,y=440)

    # Formata a tabela 
    tabela = ttk.Treeview(telaRelatorio)
    tabela.place(x=10,y=165,width=465,height=230)

    barraDeRoalgem = Scrollbar(telaRelatorio,orient='vertical',command='')
    barraDeRoalgem.place(x=465,y=165,width=15,height=230)
    tabela.configure(yscrollcommand=barraDeRoalgem.set)

    tabela['column']=("col0","col1","col2","col3")

    tabela.column("#0",width=0,minwidth=0)
    tabela.column('col0',width=96,anchor=W,minwidth=96)
    tabela.column('col1',width=96,anchor=W,minwidth=96)

    tabela.heading("#0",text="")
    tabela.heading("col0",text="Data",anchor=W)
    tabela.heading("col1",text="Hora",anchor=W)