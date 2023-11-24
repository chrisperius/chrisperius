"""
apt-get install python3-tk

import tkinter as tk

 

def mostrar_mensagem():

    label.config(text="ola, iesgo!")

 

janela = tk.Tk()

janela.title("exemplo de gui em python")

 

#criar um rotulo

 

label = tk.Label(janela, text="bem vindo a interface do usuario")

label.pack(padx= 10, pady=10)

 

#criar um botão do tipo cta  (call to action)

botao = tk.Button(janela, text="clique aqui!", command=mostrar_mensagem)

botao.pack(padx=10, pady=10)

botao.config(width=15, height=20)

 

#iniciar a gui em loop

janela.mainloop()
"""

import tkinter as tk
from tkinter import messagebox

def abrir_janela(mensagem):
    nova_janela = tk.Toplevel()
    nova_janela.title("Ação qualquer...")
    
label = tk.Label(nova_janela, text=mensagem, padx=20 pady=20) 
label.pack()

def pesquisar_produtos():
    abrir_janela('Pesquisar produto')

def checar_estoque():
    abrir_janela('Checar estoque')
    
def acrescentar_estoque():
    abrir_janela('Acrescentar estoque')
    
def remover_estoque():
    abrir_janela('Remover produto')
    
def cadastrar_produto():
    abrir_janela('Cadastrar produto')
    
# Criar janela principal

janela_principal = tk.Tk()
janela_principal.title("SISTEMA ERP IESGO")

# iconfinder.com
# Configurar ícones do menu
icon_pesquisar = tk.PhotoImage(file="lupa.png")

icon_estoque = tk.PhotoImage(file="bolsa valores.png")

icon_acrescentar = tk.PhotoImage(file="gaveta.png")

icon_remover = tk.PhotoImage(file="lixeira.png")

icon_cadastrar = tk.PhotoImage(file="envelope.png")

# Criar botões com ícone
