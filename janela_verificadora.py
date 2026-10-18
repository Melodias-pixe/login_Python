import os as os
import json
from tkinter import *
from tkinter import messagebox
from janela_principal import *
from janela_cadastro import *

class Janela_Verificadora:
    def __init__(self, janela_verificadora):
        self.janela_verificadora= janela_verificadora
        self.janela_verificadora.title("Verificacão")
        self.janela_verificadora.geometry("500x400")
        self.janela_verificadora.resizable(False, False)
        self.janela_verificadora.state("zoomed")

        self.senha_entry = StringVar()
        self.nome_entry = StringVar()

        self.iniciar_verificação()
        

    def iniciar_verificação(self):
        #Container principal:
        container = Frame(
            self.janela_verificadora, 
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

#Atribuindo o nome a atributos=============


        Nome = Label(
            card, 
            text="Insira o seu nome:", 
            font=("Arial", 10, "bold"), 
            bg="white", 
            fg="#030303"
        )
        Nome.pack(pady=(20, 5))

        self.nome_entry = Entry (
                card,
                font=("Arial", 10),
                textvariable=self.nome_entry,
                show="",
        )
        self.nome_entry.pack(pady=(0, 30))



#Atribuindo a senha a atributos=============


        Senha = Label(
            card, 
            text="Insira a sua Senha:", 
            font=("Arial", 10, "bold"), 
            bg="white", 
            fg="#030303"
        )
        Senha.pack(pady=(20, 5))

        self.senha_entry = Entry (
                card,
                font=("Arial", 10),
                textvariable=self.senha_entry,
                show="",
        )
        self.senha_entry.pack(pady=(0, 30))

        
        
        self.verificar_Json = Button(
            card,
            text="Login",
            font=("Arial", 10, "bold"),
            bg="#1100FF",
            fg="white",
            command = self.verificação_login
        )
        self.verificar_Json.pack(pady=(10, 0))
    
        self.Retornar = Button(
            card,
            text="Cadastrar-se",
            font=("Arial", 10, "bold"),
            bg="#4AFC03",
            fg="white",
            command = self.retornar_cadastro
        )
        self.Retornar.pack(pady=(10, 0))
        

    def verificação_login(self):
        if not os.path.exists("config.json"):
            self.mensageerro = messagebox.showerror("Não temos nenhum registro!")
            return 
        usuario_entry = self.nome_entry.get()
        senha__entry= self.senha_entry.get()


        with open("config.json", "r", encoding="utf-8") as arquivo:
            # json.load lê o conteúdo do arquivo e transforma de volta em um dicionário Python
            dados = json.load(arquivo)
            usuario_digitado_= dados.get("usuario", "")
            senha_digitada = dados.get("senha", "")

        if usuario_entry == usuario_digitado_ and senha__entry == senha_digitada:
            messagebox.showinfo("Sucesso!", "Login efetuado com Sucesso!")
            self.abrir_janela_principal()
        else:
            messagebox.showerror("Erro", "Usuário ou Senha Incorretors, Tente Novamente!")
            self.nome_entry.delete(0, END)
            self.senha_entry.delete(0, END)

                

    def retornar_cadastro(self):
        from janela_cadastro import Janela_Cadastro

        self.janela_verificadora.destroy()
        self.janela_cadastro = Tk()
        janela = Janela_Cadastro(self.janela_cadastro)
        self.janela_cadastro.mainloop()


    # Abrir a janela principal após o cadastro
    def abrir_janela_principal(self):
        self.janela_verificadora.destroy()
        self.janela_principal = Tk()
        janela = Janela_Principal(self.janela_principal)
        janela.janela.mainloop() 







        
        
        