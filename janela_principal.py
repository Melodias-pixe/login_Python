import os as os
import json
from tkinter import *
from tkinter import messagebox


#Janela principal após o cadastro
class Janela_Principal:
    def __init__(self, janela_principal):
        self.janela = janela_principal
        self.janela.title("Janela Principal")
        self.janela.geometry("500x400")
        self.janela.resizable(True, True)
        self.janela.state("zoomed")

        self.iniciar_janela()

    def iniciar_janela(self):
        #Container principal:
        container = Frame(
            self.janela, 
            bg="#81FFFF"
        )
        container.pack(
            pady=25, 
            padx=25, 
            fill="both", 
            expand=True
        )


        #card principal
        card = Frame(
            container, 
            bg="white",
            bd=2,
            relief="ridge"
        )
        card.pack(
            fill="both", 
            expand=True
        )

        titulo = Label(
            card, 
            text="Você concluiu o Cadastro", 
            font=("Arial", 14, "bold"), 
            bg="white", 
            fg="#030303"
        )
        titulo.pack(pady=(20, 5))

    
