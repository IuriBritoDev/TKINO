from tkinter import * 
import threading
from time import sleep
import serial
from Controller import controleUSB, controleBanco
from datetime import date
import time


ser = ' '
valorEnviado = '0'

def Input(valorBinario):
    global ser
    global valorEnviado

    if(valorBinario == 'A'):
        valorEnviado = '1'

    if(valorBinario == 'B'):
        valorEnviado = '0'

    ser.write(valorBinario.encode())

def EscreveBanco(valEscrever):

    global valorEnviado
    col = '*'
    
    Data = date.today() 
    Hora = time.strftime('%H:%M:%S', time.localtime())
    
    teste = ()
    teste = teste + (Data,)
    teste = teste + (Hora,)

    nomeDados = controleBanco.ControleLerDados('Nome', 1)
    dados = controleBanco.ControleLerDados(col,1)
    
    valorStr = str(valEscrever)
    qtDados = len(nomeDados)
    tupla = []

    size = len(valorStr)
    final_str = valorStr[:size - 2]
    
    if(qtDados != 0):
        
        for n in range(0,qtDados):

            if(dados[n][2] == '1'):
                #print('--------------')
                #print(dados[0][n])
                teste = teste +(final_str,)
            else:
                teste = teste +(valorEnviado,)
            #teste = teste +(final_str,)
        
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
