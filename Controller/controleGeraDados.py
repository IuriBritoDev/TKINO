from Controller import controleBanco
import random
from datetime import date
import time


def GeraDados():

    valores = [()]
    tupla = []
    interiros = str(random.randint(1,100))
    boleanos = str(random.choice([True, False]))
   
    Data = date.today()
    Hora = time.strftime('%H:%M:%S', time.localtime())
    
    dados = controleBanco.ControleLerDados('Nome', 1)
    qtDados = len(dados)
    
    valores = [(Data, Hora,)]
    teste = ()
    teste = teste + (Data,)
    teste = teste + (Hora,)

    if(qtDados != 0):
        
        for n in range(0,qtDados):
            
            teste = teste +(interiros,)
            
        tupla = [teste,]
        
        
    controleBanco.EscreveNaTabelaValores(tupla,qtDados)
