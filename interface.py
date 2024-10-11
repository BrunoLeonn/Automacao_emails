import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import pandas as pd
from database_manager import carregar_base_emails
from database_manager import salvar_email
from scheduler import agendar_envio

def criar_interface():
    root = tk.Tk()
    root.title("Automação de E-mails")

    # Tabela para exibir e-mails cadastrados
    tabela_frame = ttk.Frame(root)
    tabela_frame.pack(pady=10)

    colunas = ('Nome', 'Email')
    tabela = ttk.Treeview(tabela_frame, columns=colunas, show='headings')
    for col in colunas:
        tabela.heading(col, text=col)
        tabela.column(col, minwidth=0, width=200)
    tabela.pack()

    # Função para atualizar a tabela com a base de e-mails
    def atualizar_tabela():
        df = carregar_base_emails()
        for i in tabela.get_children():
            tabela.delete(i)
        for index, row in df.iterrows():
            tabela.insert("", "end", values=(row['Nome'], row['Email']))
    atualizar_tabela()

    # Seção para cadastrar novos e-mails
    form_frame = ttk.Frame(root)
    form_frame.pack(pady=10)

    ttk.Label(form_frame, text="Nome:").grid(row=0, column=0)
    entry_nome = ttk.Entry(form_frame)
    entry_nome.grid(row=0, column=1)

    ttk.Label(form_frame, text="E-mail:").grid(row=1, column=0)
    entry_email = ttk.Entry(form_frame)
    entry_email.grid(row=1, column=1)

    ttk.Button(form_frame, text="Cadastrar E-mail", command=lambda: salvar_email(entry_nome.get(), entry_email.get())).grid(row=2, columnspan=2, pady=10)

    # Seção para agendar e-mails
    enviar_frame = ttk.Frame(root)
    enviar_frame.pack(pady=10)

    # Destinatário
    global entry_destinatario, entry_horario, entry_assunto, entry_mensagem
    ttk.Label(enviar_frame, text="Destinatário:").grid(row=0, column=0)
    entry_destinatario = ttk.Entry(enviar_frame)
    entry_destinatario.grid(row=0, column=1)

    # Assunto
    ttk.Label(enviar_frame, text="Assunto:").grid(row=1, column=0)
    entry_assunto = ttk.Entry(enviar_frame)
    entry_assunto.grid(row=1, column=1)

    # Horário
    ttk.Label(enviar_frame, text="Data/Horário (dd/mm/yyyy HH:MM):").grid(row=2, column=0)
    entry_horario = ttk.Entry(enviar_frame)
    entry_horario.grid(row=2, column=1)

    # Corpo da mensagem
    ttk.Label(enviar_frame, text="Mensagem:").grid(row=3, column=0)
    entry_mensagem = scrolledtext.ScrolledText(enviar_frame, width=40, height=10)
    entry_mensagem.grid(row=3, column=1)

    # Botão de agendamento
    ttk.Button(enviar_frame, text="Agendar Envio", command=lambda: enviar_email_agendado()).grid(row=4, columnspan=2, pady=10)

    root.mainloop()

# Função de envio agendado
def enviar_email_agendado():
    destinatario_email = entry_destinatario.get()  # Captura o e-mail completo do destinatário
    horario = entry_horario.get()  # Captura o horário no formato dd/mm/yyyy HH:MM
    assunto = entry_assunto.get().strip()  # Captura o assunto do e-mail e remove quebras de linha
    mensagem = entry_mensagem.get("1.0", tk.END)  # Captura o corpo da mensagem

    # Busca o nome com base no e-mail
    df = carregar_base_emails()
    linha = df[df['Email'] == destinatario_email]  # Procura o e-mail na planilha

    if not linha.empty:
        nome = linha.iloc[0]['Nome']  # Extrai o nome da planilha com base no e-mail

        # Substitui {Nome} no texto da mensagem com o nome real
        mensagem = mensagem.replace("{Nome}", nome)

        agendar_envio(nome, destinatario_email, horario, assunto, mensagem)  # Passa o nome, o e-mail, o horário, o assunto e a mensagem
    else:
        print("Destinatário não encontrado.")
