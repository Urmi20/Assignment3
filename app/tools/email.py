import smtplib


class Email:
    @staticmethod
    def send(sender, to, subject, message, server, port, account, password):
        try:
            server = smtplib.SMTP(server, port)
            server.ehlo()
            server.starttls()
            server.login(account, password)

            header = 'From: %s \n' % sender
            header += 'To: %s \n' % to
            header += 'Cc: \n'
            header += 'Subject: %s \n\n' % subject
            message = header + message

            server.sendmail(sender, to, message)

            server.close()
        except Exception as exception:
            print(exception)
