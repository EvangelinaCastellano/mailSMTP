import ssl
import smtplib
from email.message import EmailMessage
from config import sender, password, receiver, subject, body

def send_mail(sender, password, receiver, subject, body):
    em = EmailMessage()
    em['From'] = sender
    em['To'] = receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, em.as_string())

send_mail(sender, password, receiver, subject, body)
