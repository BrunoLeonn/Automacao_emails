from datetime import datetime
import time
from email_sender import enviar_email

# Função para agendar o envio de um e-mail
def agendar_envio(nome, destinatario, horario, assunto, mensagem):
    try:
        # Tenta converter a string de horário para o formato datetime
        data_envio = datetime.strptime(horario, '%d/%m/%Y %H:%M')
    except ValueError:
        print("Formato de data/hora inválido. Use o formato dd/mm/yyyy HH:MM")
        return

    agora = datetime.now()
    segundos_esperar = (data_envio - agora).total_seconds()

    if segundos_esperar > 0:
        time.sleep(segundos_esperar)
        enviar_email(nome, destinatario, assunto, mensagem)
    else:
        print("Horário já passou. Insira um horário futuro.")
