from tkinter import *
import tkinter as tk
from tkinter import messagebox


class Janela_Cadastro:
    def __init__(self, janela_login):
        self.janela_login = janela_login
        self.janela_login.title("Login")
        self.janela_login.geometry("400x300")
        self.janela_login.resizable(True, True)

        self.iniciar_login()

    def iniciar_login(self):
        #Container principal:
        container = Frame(
            self.janela_login, 
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


        #Cadastro de usuário==============
        cadastre_usuário = Label(
            card, 
            text="Cadastre-se", 
            font=("Arial", 10, "bold"), 
            bg="white", 
            fg="#030303"
        )
        cadastre_usuário.pack(pady=(20, 5))

        self.cadastro_entry = Entry(
            card,
            font=("Arial", 10),
        )
        self.cadastro_entry.pack(pady=(0, 30))


        #Senha de usuário======================
        Senha = Label(
            card, 
            text="Senha", 
            font=("Arial", 10, "bold"), 
            bg="white", 
            fg="#030303"
        )
        Senha.pack(pady=(20, 5))

        self.senha_entry = Entry(
            card,
            font=("Arial", 10),
            show="*",
        )
        self.senha_entry.pack(pady=(0, 30))

        self.verificar = Button(
            card,
            text="Cadastrar Usuário",
            font=("Arial", 10, "bold"),
            bg="#1100FF",
            fg="white",
            command=self.verificar_cadastro,
        )
        self.verificar.pack(pady=(20, 0))


    # Verificar Cadastro de usuário e senha
    def verificar_cadastro(self):
        self.textodigitado = self.cadastro_entry.get()
        if not self.textodigitado:
            self.mensagemErro = messagebox.showerror("Erro", "Digite um nome de usuário para concluir o cadastro")
            return
        self.senhadigitada = self.senha_entry.get()
        if not self.senhadigitada:
            self.mensagemErro = messagebox.showerror("Erro", "Digite uma senha para concluir o cadastro")
            return
        self.mensagemSucesso = messagebox.showinfo("Sucesso", "Cadastro concluído com sucesso!")

class Janela_Principal:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Janela Principal")
        self.janela.geometry("400x300")
        self.janela.resizable(True, True)

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

    
