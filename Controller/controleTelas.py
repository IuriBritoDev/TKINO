from View import telaRelatorio, telaNovoProjeto, telaAbrirProjeto, telaCadastro, telaConfigura, telaConexao
from View.Painel import painelSensores, painelControladores, painelConexao


# Abre as telas da aba de seleção
def AbreTelaNovoProjeto(tela):

    telaNovoProjeto.TelaNovoProjeto(tela)      

def AbreTelaAbrirProjeto(tela):

    telaAbrirProjeto.TelaAbrirProjeto(tela) 

def AbreTelaRelatorio(tela):

    telaRelatorio.TelaRelatorio(tela)

def AbreTelaCadastro(tela):

    telaCadastro.TelaCadastro(tela) 

def AbreTelaConfigura(tela):

    telaConfigura.TelaConfigura(tela) 

def AbreTelaConexao(tela):

    telaConexao.TelaConexao(tela) 

# Abre os frames das abas
def AbreFrameSensores(frame):
    
    painelSensores.PainelSensores(frame) 

def AbreFrameControladores(frame):

    painelControladores.PainelControladores(frame) 

def AbreFrameConexao(frame):

    painelConexao.PainelConexao(frame) 