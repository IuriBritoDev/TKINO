from tkinter import *


class CriaTela():

    def __init__(self,titulo,tamanho,bg):

        self.titulo = titulo
        self.tamanho = tamanho
        self.bg = bg
        
    def parametrosTela(self):
        
        self.root = Tk()
        self.root.title(self.titulo)
        self.root.geometry(self.tamanho)
        self.root['bg'] = self.bg
        return self.root