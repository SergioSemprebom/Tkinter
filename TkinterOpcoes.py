import tkinter as tk

janela = tk.Tk() # Janela Criada

# --- PASSO 1)
# O valor checkbox_promocoes será armazenados dentro de var_promocoes ou seja em uma var AUXILIAR como parametro
var_promocoes = tk.IntVar()
checkbox_promocoes = tk.Checkbutton(text='Deseja receber e-mail promocionais?', variable=var_promocoes)
checkbox_promocoes.grid(row=0, column=0)

var_politica = tk.IntVar()
checkbox_politica = tk.Checkbutton(text='Aceita termos de Política de privacidade?', variable=var_politica)
checkbox_politica.grid(row=1, column=0)


# --- PASSO 3)
# var_promocoes é uma var AUXILIAR para gravar o texto checkbox
def enviar():
    if var_promocoes.get():
        print('Usuário deseja receber e-mail promocionais')
    else:
        print('Usuário Não deseja receber e-mail promocionais')

    if var_politica.get():
        print('Sim, o usuário aceitou a política de privacidade')
    else:
        print('NÃO, o usuário não aceitou a política de privacidade')


# --- PASSO 2)
botao_enviar = tk.Button(text='Enviar', command=enviar)
botao_enviar.grid(row=2, column=0)




janela.mainloop()