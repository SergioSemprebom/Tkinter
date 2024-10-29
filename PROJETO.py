import tkinter as tk
from tkinter import ttk # ---- PASSO 4.1.1)
from tkcalendar import DateEntry # ---- PASSO 4.2.1)


# ---- PASSO 1)
janela = tk.Tk() # Janela Criada



# ---- PASSO 4.3.2)
def pegar_cotacao():
    pass


# ---- PASSO 5.1.1)
def selecionar_aquivo():
    pass


# ---- PASSO 5.4) botao atualizar cotacoes
def atualizar_cotacoes():
    pass




# ---- PASSO 3)
# Titulo Central
janela.title('Ferramenta de Cotação de Moedas')




# ---- PASSO 4)
# Titulo 1 ------------------------ PRIMEIRO ELEMENTO -------------------------------------------------
label_cotacaomoeda = tk.Label(text='Cotação de 1 moeda especifica', borderwidth=2, relief='solid')
label_cotacaomoeda.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", columnspan=3)

# ---- PASSO 4.1)
label_selecionarmoeda = tk.Label(text='Selecionar Moeda', anchor='e')
label_selecionarmoeda.grid(row=1, column=0, padx=10, pady=10, sticky="nsew", columnspan=2)

# ---- PASSO 4.1.1)
combobox_selecionamoedas = ttk.Combobox(value=lista_moedas)
combobox_selecionamoedas.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

# ---- PASSO 4.2) 
label_selecionardia = tk.Label(text='Selecione o dia de busca da cotação', anchor='e')
label_selecionardia.grid(row=2, column=0, padx=10, pady=10, sticky="nsew", columnspan=2)


# ---- PASSO 4.2.1) 
calendario_moeda = DateEntry(year=2024, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nsew', columnspan=2)

# ---- PASSO 4.3.1)
label_textocotacao = tk.Label(text="")
label_textocotacao.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')


# ---- PASSO 4.3.2)
botao_pegarcotacao = tk.Button(text="Pegar Cotação", command=pegar_cotacao)
botao_pegarcotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nsew')


# ---- PASSO 5)
# Titulo 2 ------------------------ SEGUNDO ELEMENTO -------------------------------------------------
label_cotacaovariasmoedas = tk.Label(text='Cotaçao de Múltiplas Moedas', borderwidth=2, relief='solid')
label_cotacaovariasmoedas.grid(row=4, column=0, padx=10, pady=10, sticky="nsew", columnspan=3)

# ---- PASSO 5.1)
label_selecionaraquivo = tk.Label(text="Selecionar um Arq. em Excel com as Moedas na coluna A")
label_selecionaraquivo.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# ---- PASSO 5.1.1)
botao_selecionararquivo = tk.Button(text="Clique para Selecionar", command=selecionar_aquivo)
botao_selecionararquivo.grid(row=5, column=2, padx=10, pady=10, sticky="nsew")

# ---- PASSO 5.1.2)
label_arquivoselecionado = tk.Label(text='Nehum Arquivo Selecionado', anchor='e')
label_arquivoselecionado.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky="nsew",)

# ---- PASSO 5.2)
label_datainicial = tk.Label(text="Data Inicial", anchor='e')
label_datainicial.grid(row=7, column=0, padx=10, pady=10, sticky="nsew")

# ---- PASSO 5.2.1) calendario_datainicial
calendario_datainicial = DateEntry(year=2024, Locale='pt_br')
calendario_datainicial.grid(row=7, column=1, padx=10, pady=10, sticky="nsew")


# ---- PASSO 5.3) label_datafinal
label_datafinal = tk.Label(text="Data Final", anchor='e')
label_datafinal.grid(row=8, column=0, padx=10, pady=10, sticky="nsew")

calendario_datafinal = DateEntry(year=2024, locale='pt_br')
calendario_datafinal.grid(row=8, column=1, padx=10, pady=10, sticky="nsew")


# ---- PASSO 5.4) botao atualizar cotacoes
botao_atualizarcotacoes = tk.Button(text="Atualizar Cotações", command=atualizar_cotacoes)
botao_atualizarcotacoes.grid(row=9, column=0, padx=10, pady=10, sticky="nsew")

# ---- PASSO 5.4.1) caixa atualizar cotacoes
label_atualizarcotacoes = tk.Label(text="")
label_atualizarcotacoes.grid(row=9, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")

# ---- PASSO 5.5) botao fechar
botao_fechar = tk.Button(text="Fechar", command=janela.quit)
botao_fechar.grid(row=10, column=2, padx=10, pady=10, sticky="nsew")



# ---- PASSO 2)
janela.mainloop()