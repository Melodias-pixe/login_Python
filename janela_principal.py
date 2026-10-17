from tkinter import *
import tkinter as tk


class janela_principal:
    def __init__(self, janela_login):
        self.janela_login = janela_login
        self.janela_login.title("Login")
        self.janela_login.geometry("400x300")
        self.janela_login.resizable(False, False)

        self.iniciar_login()

    def iniciar_login(self):
        #Container principal:
        container = Frame(
            self.janela_login, 
            bg="#030303"
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
            card, text="Tela de login", 
            font=("Arial", 14, "bold"), 
            bg="white", 
            fg="#030303"
        )
