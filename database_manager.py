import pandas as pd

# Função para carregar a planilha de e-mails
def carregar_base_emails():
    try:
        df = pd.read_excel('base_emails.xlsx')  # Lê a planilha do Excel
        return df
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Nome', 'Email'])
        df.to_excel('base_emails.xlsx', index=False)
        return df

# Função para salvar um novo e-mail na base de dados
def salvar_email(nome, email):
    df = carregar_base_emails()
    novo_email = pd.DataFrame({'Nome': [nome], 'Email': [email]})
    df = pd.concat([df, novo_email], ignore_index=True)
    df.to_excel('base_emails.xlsx', index=False)
