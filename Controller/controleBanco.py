from Model import banco


# Cria variavel para o nome dos projetos
projetoAtual = " "

# Tabelas do banco 
tabelas = ['projetos','atuador', 'controlador', 'valores', 'conexao', 'configuracoes']
tabelasConexao = ['conDigDig', 'conAnaDig', 'conDigAna', 'conAnaAna']

# Tipo de colunas
colunaUltimo = ['ultimo']
colunaNome = ['Nome']
colunaContipo = ['conexao', 'tipo']
colunaDate = ['data', 'hora']
colunaSenCon =['sensor', 'controlador']
colunaPorta = ['porta']
colunaNomeVal = ['NomeControl', 'valor', 'valorMinimo', 'valorMaximo']
colunasConex = ['operaSensor', 'operaContro', 'controlOn', 'controlOff']
colunaOperador = ['operaMinSen', 'operaMaxSen', 'operaMinCon', 'operaMaxCon']
colunaValor = ['valMinSen', 'valMaxSen', 'valMinCon', 'valMaxCon']

# Tipos de dados
tipoDado = ['text', 'integer']

# Conecta ao banco Bancos
c = banco.ConexaoBanco('bancos.db')
banco.CriaTabela(c, tabelas[0])
banco.AlteraTabela(c, tabelas[0], colunaNome[0], tipoDado[0])

listaUltimo = [(projetoAtual,)]
banco.CriaTabela(c, colunaUltimo[0])
banco.AlteraTabela(c, colunaUltimo[0], colunaUltimo[0], tipoDado[0])
banco.EscreveNaTabela(c, colunaUltimo[0], colunaUltimo[0],listaUltimo,'?')

# Cria um banco de dados
def ControleCriaBanco(nomeBanco):

    nomeBanco = nomeBanco+'.db'
    inter = '?'
    projetoAtual = nomeBanco
    banco.ConexaoBanco(nomeBanco)
  
    banco.CriaTabela(c,tabelas[0])
    banco.AlteraTabela(c,tabelas[0],colunaNome[0],tipoDado[0])
   
    lista = [(nomeBanco,)]
    
    # Escreve no bancos o nome do banco
    banco.EscreveNaTabela(c,tabelas[0],colunaNome[0],lista,inter)

    # Cria as tabelas
    ControleCriaTabelas(nomeBanco)

# Cria as tabelas do novo projeto
def ControleCriaTabelas(nomeProjeto):

    con = banco.ConexaoBanco(nomeProjeto)
    
    # Cria as coluna das tabelas tabelas do novo projeto
    for n in range(1,6):
        banco.CriaTabela(con, tabelas[n])
 
    banco.AlteraTabela(con, tabelas[1], colunaNome[0], tipoDado[0])
    banco.AlteraTabela(con, tabelas[5], colunaPorta[0], tipoDado[0])

    for n in range(0,2):
        banco.AlteraTabela(con, tabelas[1], colunaContipo[n], tipoDado[0])
        banco.AlteraTabela(con, tabelas[3], colunaDate[n], tipoDado[0])
        banco.AlteraTabela(con, tabelas[4], colunaSenCon[n], tipoDado[0])
    
    for n in range(0,4):
        banco.AlteraTabela(con, tabelas[2], colunaNomeVal[n], tipoDado[0])
    
    # Cria as tabelas de conexão
    ControleCriaTabelasConex(nomeProjeto, con)

def ControleCriaTabelasConex(nomeProjeto, con):

    # Cria Tabelas de conexão e os campos sensor e controlador em todas
    for n in range(0,4):
        banco.CriaTabela(con, tabelasConexao[n])
        for m in range(0,2):
            banco.AlteraTabela(con, tabelasConexao[n], colunaSenCon[m], tipoDado[0])

    # Cria colunas nas tabelas tabelas de conexão
    for n in range(0,2):
        banco.AlteraTabela(con, tabelasConexao[0], colunasConex[n], tipoDado[0])
        banco.AlteraTabela(con, tabelasConexao[1], colunasConex[n], tipoDado[0])

    for n in range(2,4):
        banco.AlteraTabela(con, tabelasConexao[1], colunaNomeVal[n], tipoDado[0])
        banco.AlteraTabela(con, tabelasConexao[2], colunasConex[n], tipoDado[0])
    
    # Cria colunas conexão analogico analogico
    for n in range(0,4):
       banco.AlteraTabela(con, tabelasConexao[3], colunaOperador[n], tipoDado[0])
       banco.AlteraTabela(con, tabelasConexao[3], colunaValor[n], tipoDado[0])

    return projetoAtual

# pega o ultimo projeto criado
def ControlePegaProjetoAtual():

    global projetoAtual
    return projetoAtual

# Ler os dados do banco
def ControleLerDados(coluna,nTabela):

    global projetoAtual
 
    con = banco.ConexaoBanco(projetoAtual)
    dados = banco.LerTabela(con,coluna,tabelas[nTabela])
    return dados

# Mostra projetos existentes
def ControleMostraExistente():
    
    global projetoAtual    
    
    dados = banco.LerTabela(c,colunaNome[0],tabelas[0])
    return dados

# Abre projeto selecionado
def ControleAbreProjeto(projeto):

    inter = '?'
    global projetoAtual
    
    nomeProjeto = ''.join(projeto)
    projetoAtual = nomeProjeto

    lista = [(nomeProjeto,)]
    banco.DeletaDados(c, colunaUltimo[0])
    banco.EscreveNaTabela(c, colunaUltimo[0],colunaUltimo[0],lista,inter)
    
   
# Cria controladores 
def ControleCriaAtuador(valorAtuador):
    
    global projetoAtual
    interog = '?,?,?'
    
    con = banco.ConexaoBanco(projetoAtual)
    coluna = 'nome,'+'conexao,'+'tipo'
    banco.EscreveNaTabela(con, tabelas[1], coluna, valorAtuador, interog)

# Configura o controlador
def ControleConfControlador(valorControlador):

    global projetoAtual
    interog = '?,?,?,?'

    con = banco.ConexaoBanco(projetoAtual)
    coluna = ','.join(colunaNomeVal)
    banco.EscreveNaTabela(con, tabelas[2], coluna, valorControlador, interog)

# Cria controladores 
def ControleCriaConexao(valorAtuador):
    
    global projetoAtual
    interog = '?,?'
    
    con = banco.ConexaoBanco(projetoAtual)
    coluna = 'sensor,'+'controlador'
    
    banco.EscreveNaTabela(con, tabelas[4], coluna, valorAtuador, interog)

def ControleCriaConexAtuadores(nTabela, valores, interog):

    global projetoAtual
    coluna = ' '
    con = banco.ConexaoBanco(projetoAtual)

    # Conexão digital digital 
    if(nTabela == 0):

        coluna = colunaSenCon[0]+','+colunaSenCon[1]+','+colunasConex[0]+','+colunasConex[1]

    if(nTabela == 1):

        coluna = colunaSenCon[0]+','+colunaSenCon[1]+','+colunasConex[0]+','+colunasConex[1]+','+colunaNomeVal[2]+','+colunaNomeVal[3]

    if(nTabela == 2):

        coluna = colunaSenCon[0]+','+colunaSenCon[1]+','+colunasConex[2]+','+colunasConex[3]
    
    if(nTabela == 3):

        coluna = colunaSenCon[0]+','+colunaSenCon[1]+','+colunaOperador[0]+','+colunaValor[0]+','+colunaOperador[1]+','+colunaValor[1]+','+colunaOperador[2]+','+colunaValor[2]+','+colunaOperador[3]+','+colunaValor[3]
    
    banco.EscreveNaTabela(con, tabelasConexao[nTabela], coluna, valores, interog)

def ControleEscreveNaTabela(valores, interog):

    global projetoAtual
    coluna = ' '

    con = banco.ConexaoBanco(projetoAtual)
    coluna = colunaPorta[0]
    
    banco.DeletaDados(con, tabelas[5])
    banco.EscreveNaTabela(con, tabelas[5], coluna, valores, interog)

if (projetoAtual == ' '):

    dados = banco.LerTabela(c, colunaUltimo[0], colunaUltimo[0])
    
    if (dados[0] != ' '):
       
        ControleAbreProjeto(dados[0])