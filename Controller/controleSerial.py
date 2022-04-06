from tkinter import * 
import threading
from time import sleep
import serial
from Controller import controleUSB, controleBanco
from datetime import date
import time

ser = ' '

def EscreveBanco(valEscrever):

    Data = date.today() 
    Hora = time.strftime('%H:%M:%S', time.localtime())
    
    teste = ()
    teste = teste + (Data,)
    teste = teste + (Hora,)

    dados = controleBanco.ControleLerDados('Nome', 1)
    
    valorStr = str(valEscrever)
    qtDados = len(dados)
    tupla = []

    size = len(valorStr)
    final_str = valorStr[:size - 2]
    
    if(qtDados != 0):
        
        for n in range(0,qtDados):
                
            teste = teste +(final_str,)
        
        tupla = [teste,]

        controleBanco.EscreveNaTabelaValores(tupla,qtDados)

def repete():
    
    global ser
    
    while True:
        if(ser != ' '):
        
            valores = ser.readline().decode('ascii')
        
            pjtAtual = controleBanco.ControlePegaProjetoAtual()

            if(pjtAtual != ' '):
                
                EscreveBanco(valores)
            
        sleep(1)

t = threading.Thread(target=repete)
t.setDaemon(True)
t.start()
