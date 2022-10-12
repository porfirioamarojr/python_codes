import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#corpo da mensagem do email
msg = MIMEMultipart()
message = "Você Recebeu um email"

recipients = 'email1@gmail.com,email2@hotmail.com,email3@outlook.com'
sender = 'email_remetente'
#Credenciais do email_remetente e assunto
password = "********"
msg['From'] = sender 
msg['To'] = recipients
msg['Subject'] = "Só sucesso"

#Monta conexão e envia email
msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', port=587)
server.starttls()
server.login(sender, password)
server.sendmail(sender,recipients.split(','), msg.as_string())
server.quit()
