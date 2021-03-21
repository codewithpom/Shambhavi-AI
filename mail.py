import smtplib
from email.message import EmailMessage
import time
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server_login_mail = 'padmashreejha717@gmail.com'
server_login_password = 'pankaj@2016'
server.login(server_login_mail, server_login_password)
i = 0
def send_email(rec, subject, message):
    email = EmailMessage()
    email['From'] = server_login_mail
    email['To'] = rec
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    return 'Successfully sent mail'




