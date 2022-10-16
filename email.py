print('Avaliação email')
import email.message
import smtplib

login = 'kleciafarias477@gmail.com'
senha = 'k123456el'

assunto =input('Assunto do Email: ')
remetente = input('E-mail do remetente: ')
destinatario = input('E-mail do destinatário: ')
mensagem = input('Escreva sua mensagem: ')

msg = email.message.Message()
msg['Subject'] = assunto
msg['From'] = remetente
msg['To'] = destinatario
msg.add_header('Content-Type','text/html')
msg.set_payload(mensagem)



enviar_email= smtplib.SMTP('smtp.gmail.com:587')
enviar_email.starttls()
enviar_email.login(login,senha)
enviar_email.sendmail(msg['From'],msg['To'], msg.as_string().encode('utf-8'))


print('Email Enviado')