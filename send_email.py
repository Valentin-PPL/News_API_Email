import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "gastonvalentino@gmail.com"
    password = "lzkthnwbmntykzne"

    receiver = "ioanarox86@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


send_email("Hello, how are you?")