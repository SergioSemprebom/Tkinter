import tkinter as tk

janela = tk.Tk() # Janela Criada


# --- Passo 2)
# Conectando os tres botões a uma variavel, onde no valor (value= xxxxxxxxx) posso colocar um nome sugestivo
# O valor dentro da tk.StringVar(value="Vazio") indica que nenhum valor vem marcado no RadioButton
var_aviao = tk.StringVar(value="Vazio")


# --- Passo 1)
# Botões

botao_classeeconomica = tk.Radiobutton(text="Classe Economica", variable=var_aviao, value="Classe Economica")
botao_classeexecutiva = tk.Radiobutton(text="classe Executiva", variable=var_aviao, value="Classe Executiva")
botao_primeiraclasse = tk.Radiobutton(text="Primeira Classe", variable=var_aviao, value="Classe Classe")
botao_classeeconomica.grid(row=0, column=0)
botao_classeexecutiva.grid(row=0, column=1)
botao_primeiraclasse.grid(row=0, column=2)



# --- Passo 4)
# A funcao que print o tipo da classe, SEM a necessidade do if
def enviar():
    print(var_aviao.get())



# --- Passo 3)
# imprimindo o botão para visualizar a informacao
botao_enviar = tk.Button(text='Enviar', command=enviar)
botao_enviar.grid(row=1, column=0)


janela.mainloop()


