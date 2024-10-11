import smtplib
from email.message import EmailMessage
from segredos import senha



# Função para enviar o e-mail
def enviar_email(nome, destinatario, assunto, mensagem):
    #Configurar email, senha
    EMAIL_ADDRESS = 'mail@exemplo.com'
    EMAIL_PASSWORD = senha

    # Criar um e-mail
    msg = EmailMessage()
    msg['Subject'] = assunto
    msg['From'] = EMAIL_ADDRESS
    msg['to'] = destinatario
    msg.set_content(mensagem)

    # Enviar um e-mail
    with smtplib.SMTP_SSL('mail.gmail.com',365) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    
    print(f"E-mail enviado para {nome} ({destinatario}) com sucesso.")