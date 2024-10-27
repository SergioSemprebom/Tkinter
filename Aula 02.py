import tkinter as tk


janela = tk.Tk() # janela criada

janela.title("Cotação de Moedas")# ------------------------------------ Criando um titulo

janela.rowconfigure(0, weight=1)# ajuste automaticamente (linha pra baixo, sim-automatico=1)
janela.columnconfigure([0, 1], weight=1)# ajuste automaticamente (coluna pra direita, sim-automatico=1)

mensagem = tk.Label(text="Sistema de Busca de cotacao de Moedas", background='#7e40c8')# ---- Passo 1) Criar Objeto 
mensagem.grid(row=0, column=0, columnspan=2, sticky='nsew') # ---------- Passo 2) colocar o objeto dentro da janela

# row=0 qtas linhas vai ser ocupada
# columnspan=2 qtas colunas serão ocupadas
# sticky='nsew' centralizar

mensagem2 = tk.Label(text="Selecione a moeda desejada", foreground='black')# letra verde
mensagem2.grid(row=1, column=0)


moeda = tk.Entry()
moeda.grid(row=1, column=1)


# loop padrao em que o tkroda o tempo inteiro
janela.mainloop()
moeda.gat
