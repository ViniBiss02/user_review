# Importa o módulo principal do Tkinter para criar interfaces gráficas
import csv
import time
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

def salvar_avaliacao(tipo_avaliacao, texto_opiniao):
    caminho_csv = os.path.join('D:/py_train/user_review', 'review_usuarios.csv')
    # Se o arquivo não existe, cria com cabeçalho
    arquivo_existe = os.path.exists(caminho_csv)
    with open(caminho_csv, mode='a', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo)
        if not arquivo_existe:
            writer.writerow(['Avaliacao', 'Opiniao'])
        writer.writerow([tipo_avaliacao, texto_opiniao])

# Cria a janela principal com o tema \*darkly\*
satisfaction = ttk.Window(themename="darkly")
# Define o título da janela que aparecerá na barra de título
satisfaction.title("Review User")

satisfaction.resizable(False, False)

# Cria o \*frame_review\*, que será a tela inicial onde o usuário escolhe a avaliação
frame_review = ttk.Frame(satisfaction)
# Posiciona o frame na linha 0, coluna 0, ocupando todo o espaço disponível (nsew = norte, sul, leste, oeste)
frame_review.grid(row=0, column=0, sticky="nsew")

# Cria o \*frame_feedback\*, a tela onde o usuário poderá digitar sugestões de melhoria
frame_feedback = ttk.Frame(satisfaction)
# Posiciona o frame_feedback na mesma posição que o frame_review para facilitar a troca de telas
frame_feedback.grid(row=0, column=0, sticky="nsew")

frame_thanks = ttk.Frame(satisfaction)

frame_thanks.grid(row=0, column=0, sticky="nsew")

# Função \*show_frame\* que recebe um frame e chama o método tkraise() para mostrá-lo na tela
def show_frame(frame):
    frame.tkraise()  # Traz o \*frame\* para o topo, tornando-o visível

# Função \*change_window\* que troca a tela para o frame_feedback, chamando show_frame
def change_window():
    show_frame(frame_feedback)

def thanks_window():
    show_frame(frame_thanks)

def out_window():
    text_feedback.config(state=tk.DISABLED)
    time.sleep(3)
    show_frame(frame_review)

# Cria um objeto Style para personalizar o estilo dos widgets
style = ttk.Style()
# Configura um \*estilo customizado\* chamado "Custom.TButton" com a fonte Arial tamanho 20
style.configure("Custom.TButton", font=("Arial", 20))

# ==================== Conteúdo do \*frame_review\* ====================

def enviar_great():
    salvar_avaliacao('Great', '')
    show_frame(frame_thanks)

def enviar_good():
    texto = text_feedback.get("1.0", "end").strip()
    salvar_avaliacao('Good', texto)
    show_frame(frame_review)

def enviar_regular():
    texto = text_feedback.get("1.0", "end").strip()
    salvar_avaliacao('Regular', texto)
    show_frame(frame_review)

def enviar_bad():
    texto = text_feedback.get("1.0", "end").strip()
    salvar_avaliacao('Bad', texto)
    show_frame(frame_review)

# Cria um rótulo (label) com o título da tela de avaliação
tittle = ttk.Label(frame_review, text="Deixe aqui a sua avaliação!", font=("Helvetica", 34))
# Posiciona o rótulo com um espaçamento vertical (pady) de 20 pixels

# Cria um botão \*Great\* com o estilo \*success\*
great_review = ttk.Button(
    frame_review,                   # Define que o botão ficará dentro do \*frame_review\*
    text="😃      Great",           # Texto exibido no botão
    bootstyle="success",            # Aplica o estilo \*success\* definido pelo ttkbootstrap
    width=50,                       # Define a largura do botão
    padding=20,                     # Define o espaçamento interno do botão (padding)
    command=enviar_great          # Associa a ação de mudar a tela ao clicar no botão
)
# Posiciona o botão garantindo um espaçamento vertical de 10 pixels

# Cria um botão \*Good\* que ao ser clicado chama a função change_window para trocar a tela
good_review = ttk.Button(
    frame_review,
    text="🙂       Good",
    bootstyle="info",               # Estilo \*info\*
    width=50,
    padding=20,
    command=enviar_good          # Associa a ação de mudar a tela ao clicar no botão
)

# Cria o botão \*Regular\* com estilo \*warning\*, também configurado para trocar a tela
regular_review = ttk.Button(
    frame_review,
    text="😐    Regular",
    bootstyle="warning",            # Estilo \*warning\*
    width=50,
    padding=20,
    command=enviar_regular
)

# Cria o botão \*Bad\* com o estilo \*danger\* que também chama change_window ao clicar
bad_review = ttk.Button(
    frame_review,
    text="😖        Bad",
    bootstyle="danger",             # Estilo \*danger\*
    width=50,
    padding=20,
    command=enviar_bad
)
tittle.pack(pady=20)
great_review.pack(pady=10)
good_review.pack(pady=10)
regular_review.pack(pady=10)
bad_review.pack(pady=10)

# Configuração opcional para definir estilos específicos com fonte tamanho 25 para cada tipo de botão
satisfaction.style.configure('success.TButton', font=(None, 25))
satisfaction.style.configure('info.TButton', font=(None, 25))
satisfaction.style.configure('warning.TButton', font=(None, 25))
satisfaction.style.configure('danger.TButton', font=(None, 25))

# ==================== Conteúdo do \*frame_feedback\* ====================

# Cria um rótulo para o feedback solicitando melhorias
feedback_label = ttk.Label(frame_feedback, text="O que pode melhorar?", font=("Helvetica", 24))
# Posiciona o rótulo com um espaçamento vertical de 20 pixels
feedback_label.pack(pady=20)

# Cria uma caixa de texto onde o usuário pode inserir o seu feedback
text_feedback = tk.Text(frame_feedback, width=50, height=10)
# Posiciona a caixa de texto com um espaçamento vertical de 10 pixels
text_feedback.pack(pady=10)

# Cria o botão \*Enviar\* que ao ser clicado chama a função enviar_good
send_button = ttk.Button(
    frame_feedback,
    text="Enviar",
    bootstyle="success",           # Estilo \*success\*
    width=50,
    padding=20,
    command=out_window()            # Associa a ação de enviar a avaliação ao clicar no botão
)
send_button.pack(pady=10)

# Cria o botão \*Voltar\* que retorna para a tela de avaliação (\*frame_review\*)
back_button = ttk.Button(
    frame_feedback,
    text="Voltar",
    bootstyle="info",               # Estilo \*info\*
    width=50,
    padding=20,
    # Define uma função lambda que chama show_frame para exibir o \*frame_review\*
    command=lambda: show_frame(frame_review)
)
back_button.pack(pady=10)

# ==================== Conteúdo do \*frame_thanks\* ====================
# Cria um rótulo de agradecimento
thanks_label = ttk.Label(frame_thanks, text="Obrigado pela sua avaliação!", font=("Helvetica", 24))
choice_review_label = ttk.Label(frame_thanks, text="Deseja deixar um elogio para o restaurante ?", font=("Helvetica", 18))

review_button = ttk.Button(
    frame_thanks,
    text="Deixar um elogio",
    bootstyle="info",               # Estilo \*info\*
    width=50,
    padding=20,
    command=change_window          # Associa a ação de mudar a tela ao clicar no botão
)

out_button = ttk.Button(
    frame_thanks,
    text="voltar para tela inicial",
    bootstyle="warning",               # Estilo \*info\*
    width=50,
    padding=20,
    command=lambda: show_frame(frame_review)          # Associa a ação de mudar a tela ao clicar no botão
)
# Posiciona o rótulo com um espaçamento vertical de 20 pixels
thanks_label.pack(pady=20)
# Posiciona o rótulo com um espaçamento vertical de 10 pixels
choice_review_label.pack(pady=25)
review_button.pack(pady=10)
out_button.pack(pady=10)

# Inicialmente, exibe o \*frame_review\* para que a tela de avaliação seja a primeira a ser vista
show_frame(frame_review)

# Inicia o loop principal da interface, permitindo que a janela permaneça aberta e interativa
satisfaction.mainloop()