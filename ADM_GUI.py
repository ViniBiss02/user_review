# Importa o módulo tkinter, que é a biblioteca padrão para interfaces gráficas em Python
import tkinter as tk
# Importa o módulo ttkbootstrap, que melhora os widgets do Tkinter com temas modernos
import ttkbootstrap as ttk
import os
from openpyxl import Workbook

# Caminho da pasta onde procurar o arquivo
pasta = 'D:/py_train/user_review'

# Nome do arquivo que queremos encontrar ou criar
nome_arquivo = 'review_usuarios.csv'
caminho_arquivo = os.path.join(pasta, nome_arquivo)

# Verifica se o arquivo já existe na pasta
if not os.path.exists(caminho_arquivo):
    # Se não existir, cria um arquivo Excel
    wb = Workbook()
    wb.save(caminho_arquivo)
    print(f'Arquivo {nome_arquivo} criado.')
else:
    print(f'Arquivo {nome_arquivo} já existe.')

# Cria a janela principal com o tema \*darkly\*
admin = ttk.Window(themename="darkly")
# Define o título da janela que aparecerá na barra de título
admin.title("Painel Admin")
# Define o tamanho da janela para 800x600 pixels
admin.geometry("800x600")
# Impede que a janela seja redimensionada pelo usuário
admin.resizable(False, False)

# Cria o \*frame_admin\*, que será a tela inicial onde o admin pode ver as avaliações
frame_admin = ttk.Frame(admin)
# Posiciona o frame na linha 0, coluna 0, ocupando todo o espaço disponível (nsew = norte, sul, leste, oeste)
frame_admin.grid(row=0, column=0, sticky="nsew")

admin.mainloop()