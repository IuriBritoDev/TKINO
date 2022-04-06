from View import telaRelatorio, telaNovoProjeto, telaAbrirProjeto, telaCadastro, telaConfigura, telaConexao, telaEditarControle, telaPopUp
from View.Painel import painelSensores, painelControladores, painelConexao
from View.Conexao import telaConAnalogAnalog, telaConAnalogDigit, telaConDigitAnalog, telaConDigitDigit 


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

# Abre telas de conexões de atuadores
def AbreTelaConAnAn(tela):

    telaConAnalogAnalog.TelaConAnalogAnalog(tela) 

def AbreTelaConAnDig(tela):

    telaConAnalogDigit.TelaConAnalogDig(tela)

def AbreTelaConDigAn(tela):

    telaConDigitAnalog.TelaConDigAnalog(tela)

def AbreTelaConDigDig(tela):

    telaConDigitDigit.TelaConDigDig(tela)

# Abre os frames das abas
def AbreFrameSensores(frame):
    
    painelSensores.PainelSensores(frame) 

def AbreFrameControladores(frame, tela):

    painelControladores.PainelControladores(frame, tela) 

def AbreFrameConexao(frame, tela):

    painelConexao.PainelConexao(frame, tela) 

# Abre telas de edição da conexão e controladores 
def AbreEditorControlador(tela, controle):
    
    telaEditarControle.TelaEditarControle(tela, controle)

# Abre telas de PopUP
def AbrePopUp(tela, mensagem):
    
    telaPopUp.TelaPopUp(tela, mensagem)