import sqlite3


# Conecta o banco de dados
def ConexaoBanco(conexao):

    banco = None
    try:
        banco = sqlite3.connect(conexao)
    except sqlite3.Error as ex:
        print(ex)
    return banco

# Executa comandos no banco
def ComandoBanco(conexao, sql):

    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except sqlite3.Error as ex:
        print(ex)

# Cria tabelas no banco
def CriaTabela(conexao, tabela):

    try:
        c = conexao.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS "+tabela+" (id integer PRIMARY KEY)")
        conexao.commit()
    except sqlite3.Error as ex:
        print(ex)

# Escreve na tabela
def EscreveNaTabela(conexao, nomeTabela, nomeColuna, valores, interogacao):
    
    try:
        c=conexao.cursor()
        c.executemany("INSERT INTO "+nomeTabela+" ("+nomeColuna+") VALUES("+interogacao+")",valores)
        conexao.commit()
    except sqlite3.Error as ex:
        print(ex)

# Ler dados da tabela
def LerTabela(conexao, coluna, nomeTabela):
    
    resultado = " "
    try:
        c = conexao.cursor()
        c.execute("SELECT "+coluna+" FROM "+nomeTabela+"")
        resultado = c.fetchall()
        
    except sqlite3.Error as ex:
        print(ex)
    return resultado

# Altera tabela existente
def AlteraTabela(conexao, nomeTabela,nomeColuna, tipo):

    try:
        c=conexao.cursor()
        c.execute("ALTER TABLE "+nomeTabela+" ADD COLUMN "+nomeColuna+" "+tipo+"")
        conexao.commit()
    except sqlite3.Error as ex:
        print(ex)

# Deleta os dados de uma tabela
def DeletaDados(conexao, tabela):

    try:
        c = conexao.cursor()
        c.execute("DELETE FROM "+tabela+"")
        conexao.commit()
    except sqlite3.Error as ex:
        print(ex)

# Busca a primeira lina de uma tabela
def BuscaPrimeirosDados(conexao, tabela):

    resultado = " "
    try:
        c = conexao.cursor()
        c.execute("SELECT * FROM "+tabela+" ORDER BY ROWID ASC LIMIT 1")
        resultado = c.fetchall()

    except sqlite3.Error as ex:
        print(ex)
    return resultado

# Busca os ultimos dados de uma tabela
def BuscaUltimosDados(conexao, tabela):

    resultado = " "
    try:
        c = conexao.cursor()
        c.execute("SELECT * FROM "+tabela+" WHERE ID = (SELECT MAX(ID)  FROM "+tabela+")")
        resultado = c.fetchall()
    except sqlite3.Error as ex:
        print(ex)
    return resultado

# Busca os dados dentro de duas datas
def BuscaDadosPorId(conexao, tabela, idI, idF):
    
    resultado = " "
    try:
        c = conexao.cursor()
        c.execute("SELECT * FROM "+tabela+" where id between "+idI+" and "+idF+"")
        resultado = c.fetchall()

    except sqlite3.Error as ex:
        print(ex)
    return resultado