import os as os
import json
from tkinter import *
from tkinter import messagebox
from janela_principal import *


class Janela_Verificadora:
    def __init__(self, janela_verificadora):
        self.janela_verificadora= janela_verificadora
        self.janela_verificadora.title("Verificacão")
        self.janela_verificadora.geometry("500x400")
        self.janela_verificadora.resizable(False, False)
        
        #Container principal:
        container = Frame(
            self.janela_cadastro, 
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
            text="Tela de login", 
            font=("Arial", 14, "bold"), 
            bg="white", 
            fg="#030303"
        )
        titulo.pack(pady=(20, 5))
        
        
        self.deletar_Json = Button(
                card,
                text="Deletar registros anteriores",
                font=("Arial", 10, "bold"),
                bg="#FF0000",
                fg="white",
                command=self.deletar_json,
            )
        self.deletar_Json.pack(pady=(20, 0))