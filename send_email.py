import smtplib, ssl
from email.message import EmailMessage


def send_email(message_text):
    host = "smtp.gmail.com"
    port = 465

    username = "gastonvalentino@gmail.com"
    password = "lzkthnwbmntykzne"

    receiver = "ioanarox86@gmail.com"
    msg = EmailMessage()
    msg["From"] = username
    msg["To"] = receiver
    msg["Subject"] = "Latest News"
    msg.set_content(message_text)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.send_message(msg)


