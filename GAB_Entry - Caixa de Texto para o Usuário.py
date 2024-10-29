import tkinter as tk

janela = tk.Tk()

janela.title("Cotação de Moedas")

mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas", fg='white', bg='black', width=50, height=10)
mensagem.pack()

mensagem2 = tk.Label(text="Selecione a moeda desejada", height=15, width=70)
mensagem2.pack()

janela.mainloop()

