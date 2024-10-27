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

#  ------- CRIAR A FUNCAO SEMPRE ANTES DO BOTAO ASSOCIADA A SUA FUNCAO ------------

dicionario_cotacoes = {
    'Dólar' : 5.67,
    'Euro ': 6.78,
    'Bitcoin' : 123.45

}

def busca_cotacao(): # a funcao dentro do Tkinter tem acesso a todos os paramentros do Tkinter
    moeda_preenchida = moeda.get()# o get vai pegar a informacao dentro da caixa texto da moeda, será o texto q user preencheu
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)# verificando o dicionario

    # verificando se encntrou o resultado no dicionario
    mensagem_cotacao = tk.Label(text="Cotaçao não encontrada")
    mensagem_cotacao.grid(row=3, column=0)
    if cotacao_moeda:
        mensagem_cotacao["text"] = f"A cotacao de {moeda_preenchida} é de {cotacao_moeda} reais"


botao = tk.Button(text="Buscar Cotacao",command=busca_cotacao)
botao.grid(row=2, column=1)


# loop padrao em que o tkroda o tempo inteiro
janela.mainloop()

