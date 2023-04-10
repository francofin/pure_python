import smtplib, ssl


def send_an_email(message):

    host = "smtp.gmail.com"
    port = 465
    username = "francoiskieran89@gmail.com"
    password = "ghrjdykldqeqbihq"
    receiver = "francoiskieran89@gmail.com"
    message = message
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


