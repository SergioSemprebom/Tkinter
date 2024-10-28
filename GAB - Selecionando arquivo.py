from tkinter.filedialog import askopenfilename
import pandas as pd


# --- Passo 1)
caminho_arquivo = askopenfilename(title="Selecione um arquivo Excel para abrir")

# --- Passo 2)
df = pd.read_excel(caminho_arquivo)

print(df)
