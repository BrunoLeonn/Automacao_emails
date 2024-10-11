import os
import smtplib
from email.message import EmailMessage
from segredos import senha

#Configurar email, senha
EMAIL_ADDRESS = 'brunocam2025@gmail.com'
EMAIL_PASSWORD = senha

# Criar um e-mail
msg = EmailMessage()
msg['Subject'] = 'Carga #35 chegou ao porto'
msg['From'] = 'brunocam2025@gmail.com'
msg['to'] = 'brunocam2025@gmail.com'
msg.set_content('Favor buscar a carga #35 que acaba de chegar na portaria')

# Enviar um e-mail
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)