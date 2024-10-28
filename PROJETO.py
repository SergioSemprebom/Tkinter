import tkinter as tk
from tkinter import ttk # ---- PASSO 4.1.1)
from tkcalendar import DateEntry # ---- PASSO 4.2.1)


lista_moedas = ['Dólar', 'Euro', 'Bitcoin'] # ---- PASSO 4.1.1)

# ---- PASSO 1)
janela = tk.Tk() # Janela Criada



# ---- PASSO 4.3.2)
def pegar_cotacao():
    pass

# ---- PASSO 3)
# Titulo Central
janela.title('Ferramenta de Cotação de Moedas')




# ---- PASSO 4)
# Titulo 1 ------------------------ PRIMEIRO ELEMENTO -------------------------------------------------
label_cotacaomoeda = tk.Label(text='Cotação de 1 moeda especifica', borderwidth=2, relief='solid')
label_cotacaomoeda.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", columnspan=3)

# ---- PASSO 4.1)
label_selecionarmoeda = tk.Label(text='Selecionar Moeda')
label_selecionarmoeda.grid(row=1, column=0, padx=10, pady=10, sticky="nsew", columnspan=2)

# ---- PASSO 4.1.1)
combobox_selecionamoedas = ttk.Combobox(value=lista_moedas)
combobox_selecionamoedas.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

# ---- PASSO 4.2) 
label_selecionarmoeda = tk.Label(text='Selecione o dia de busca da cotação')
label_selecionarmoeda.grid(row=2, column=0, padx=10, pady=10, sticky="nsew", columnspan=2)


# ---- PASSO 4.2.1) 
calendario_moeda = DateEntry(year=2021, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nsew', columnspan=2)

# ---- PASSO 4.3.1)
label_textocotacao = tk.Label(text = "")
label_textocotacao.grid(row=3, columnn=0, padx=10, pady=10, sticky='nsew', columnspan=2)

# ---- PASSO 4.3.2)
botao_pegarcotacao = tk.Button(text="Pegar Cotação", command=pegar_cotacao)
botao_pegarcotacao.grid(row=3, columnn=2, padx=10, pady=10, sticky='nsew')

# ---- PASSO 5)
# Titulo 2 ------------------------ SEGUNDO ELEMENTO -------------------------------------------------
label_cotacaovariasmoedas = tk.Label(text='Cotação de multiplas moedas', borderwidth=2, relief='solid')
label_cotacaovariasmoedas.grid(row=4, column=0, padx=10, pady=10, sticky="nsew", columnspan=3)






# ---- PASSO 2)
janela.mainloop()