import os as os
import json
from tkinter import *
from tkinter import messagebox
from janela_principal import *
from  janela_verificadora import *


class Janela_Cadastro:
    def __init__(self, janela_cadastro):
        self.janela_cadastro = janela_cadastro
        self.janela_cadastro.title("Cadastro")
        self.janela_cadastro.geometry("500x400")
        self.janela_cadastro.resizable(True, True)

        # Variável para o checkbutton "Lembrar-me", senha e cadastro
        self.lembrar_check = BooleanVar()
        self.senha_entry = StringVar()
        self.cadastro_entry = StringVar()

        self.iniciar_login()

        

    def iniciar_login(self):
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
            textvariable=self.cadastro_entry
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
            textvariable=self.senha_entry,
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


# Checkbutton lembrar-me===============
        self.check_lembrar = Checkbutton(
            card,
            text="Lembrar-me",
            font=("Arial", 10),
            bg="white",
            fg="#030303",
            variable=self.lembrar_check
        )
        self.check_lembrar.pack(pady=(10, 0))
        self.verificacao = Button(
            card,
            text="Login",
            font=("Arial", 10, "bold"),
            bg="#1E12CA",
            fg="white",
            command=self.verificação,
        )
        self.verificacao.pack(pady=(20, 0))

        

# Deletar Json de uma vez para criar outra conta
        
        



# Verificar Cadastro de usuário e senha e checkbutton lembrar-me================
    def verificar_cadastro(self):
        if not self.cadastro_entry.get():
            self.mensagemErro = messagebox.showerror("Erro", "Digite um nome de usuário para concluir o cadastro")
            return
        if not self.senha_entry.get():
            self.mensagemErro = messagebox.showerror("Erro", "Digite uma senha para concluir o cadastro")
            return
        if len(self.senha_entry.get()) < 9:
            self.mensagemErro = messagebox.showerror("Erro", "A senha deve ter pelo menos 9 caracteres")
            return
        if self.lembrar_check.get():
            self.salvar_Json()
        self.mensagemSucesso = messagebox.showinfo("Sucesso", "Cadastro concluído com Sucesso!")
        self.abrir_janela_principal()


    def verificação(self):
        if os.path.exists("config.json"):
            self.abrir__janela_verificadora
        else:
            self.mensagemSucesso = messagebox.showerror("Login não Encontrado", "Seu Login não foi encontrado, por favor, faça um")

    
#JSON======================
    def salvar_Json(self):
        # Lógica para lembrar o usuário
        senha = self.senha_entry.get()
        cadastro = self.cadastro_entry.get()

        #Valores:
        self.Dados = {
            "usuario": cadastro,
            "senha": senha
        }
        with open("config.json", "w", encoding="utf-8") as Dados:
        # json.dump pega o dicionário 'dados' e o escreve dentro do 'Dados'
            json.dump(self.Dados, Dados, indent=4) 
            
        self.mensagemSucesso = messagebox.showinfo("Sucesso","Login salvo com Sucesso!")



    def restaurar_Json(self):
        if os.path.exists("config.json"):
            with open("config.json", "r", encoding="utf-8") as arquivo:
                # json.load lê o conteúdo do arquivo e transforma de volta em um dicionário Python
                dados = json.load(arquivo)
                
                # Insere os dados recuperados de volta nos campos Entry do Tkinter
                self.cadastro_entry.set(dados.get("usuario", ""))
                self.senha_entry.set(dados.get("senha", ""))
                self.abrir_janela_principal()



# Abrir a janela principal após o cadastro
    def abrir_janela_principal(self):
        self.janela_cadastro.destroy()
        self.janela_principal = Tk()
        janela = Janela_Principal(self.janela_principal)
        janela.janela.mainloop() 

# Abrir janela verificadora
    def abrir__janela_verificadora(self):
        self.janela_cadastro.destroy()
        self.janela_verificadora = Tk()
        janela = Janela_Verificadora(self.janela_verificadora)
        janela.janela_verificadora.mainloop()