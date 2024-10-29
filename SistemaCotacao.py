import tkinter as tk
from tkinter import ttk # ---- PASSO 4.1.1)
from tkcalendar import DateEntry # ---- PASSO 4.2.1)
from tkinter.filedialog import askopenfilename # ---- PASSO 5.1.1)
import pandas as pd # ---- PASSO 5.1.2)
import requests # --- PASSO 6)
from datetime import datetime # --- PASSO 6)
import numpy as np



# --- PASSO 6)
# --- Sistema de Cotação de moedas com API
requisicao = requests.get('https://economia.awesomeapi.com.br/json/all')
dicionario_moedas = requisicao.json()# vai transformar o dicionario json em um dict python
lista_moedas = list(dicionario_moedas.keys())


# ---- PASSO 4.3.2)
def pegar_cotacao():
    moeda = combobox_selecionamoedas.get()
    data_cotacao = calendario_moeda.get()
    ano = data_cotacao[-4:]# quatro ultimo digitos 2024
    mes = data_cotacao[3:5]# indice tres até o indice cinco
    dia = data_cotacao[:2] # até o indice dois( mais nao pega o indice 2)
    link = f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}'
    requisicao_moeda = requests.get(link)
    cotacao = requisicao_moeda.json()
    valor_moeda = cotacao[0]['bid']# utilizando o link(var_cotacao) -> cotacao[0] -> é o dict
    label_textocotacao['text'] = f'A cotação da {moeda} no dia {data_cotacao} é de: R${valor_moeda}'

# ---- PASSO 5.1.1)
def selecionar_aquivo():
    caminho_arquivo = askopenfilename(title='Selecione o Arquivo de Moeda')
    # preciso a armazenar a info do caminho do arquivo na variavel do tkinter
    var_caminhoarquivo.set(caminho_arquivo)

# ---- PASSO 5.4) botao atualizar cotacoes
def atualizar_cotacoes():
    #le o df de moeda
    df =pd.read_excel(var_caminhoarquivo.get())
    moedas = df.iloc[:, 0] #[indice, coluna]
    #pegar a data de inicio e data de fim da cotacoes
    data_inicial = calendario_datainicial.get()
    data_final = calendario_datafinal.get()
    ano_inicial = data_inicial[-4:]
    mes_inicial = data_inicial[3:5]
    dia_inicial = data_inicial[:2]

    ano_final = data_final[-4:]
    mes_final = data_final[3:5]
    dia_final = data_final[:2]
    for moeda in moedas:
        link = f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?' \
               f'start_date={ano_inicial}{mes_inicial}{dia_inicial}&' \
                f'end_date={ano_final}{mes_final}{dia_final}'
        requisicao_moeda = requests.get(link)
        cotacoes = requisicao_moeda.json()
        for cotacao in cotacoes:
            timestamp = int(cotacao['timestamp'])
            bid = float(cotacao['bid'])
            data = datetime.timestamp(timestamp)
            data = datetime.strtime('%d/%m/%Y')
            if data in df:
                df[data] = np.nan
            df.loc[df.iloc[:, 0] == moeda, data] = bid
    df.to_excel("Teste.xlsx")
    label_atualizarcotacoes['text'] = 'Arquivo Atualizado com Sucesso!'


# ---- PASSO 1)
janela = tk.Tk() # Janela Criada

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

# utilizamos
var_caminhoarquivo = tk.StringVar()


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