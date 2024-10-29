import tkinter as tk
from tkinter import ttk # ---- PASSO 4.1.1)
from tkcalendar import DateEntry # ---- PASSO 4.2.1)
from tkinter.filedialog import askopenfilename # ---- PASSO 5.1.1)
import requests # --- PASSO 6)

# --- PASSO 6)
# --- Sistema de Cotação de moedas com API
requisicao = requests.get('https://economia.awesomeapi.com.br/json/all')
dicionario_moedas = requisicao.json()# vai transformar o dicionario json em um dict python
lista_moedas = list(dicionario_moedas.keys())


# ---- PASSO 1)
janela = tk.Tk() # Janela Criada



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
    if caminho_arquivo:
        label_arquivoselecionado['text'] = f'Arquivo Selecionado: {caminho_arquivo}'




# ---- PASSO 5.4) botao atualizar cotacoes
def atualizar_cotacoes():
    # ler o df de moeda
    # pegar a data de inicio e data de fim da cotacoes
    # para cada noeda
        # pegar todas as cotacoes daquela moeda
        # criar uma coluna em novo dataframe com todas as cotacoes daquela moeda
    # criar um arquivo com todas as cotacoes




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

# utilizamos na aula do RadioButon
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