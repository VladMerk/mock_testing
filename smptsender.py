import smtplib
from email.message import EmailMessage


class EmailSender:
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()

    def login(self) -> bool:
        self.server.login(self.email, self.password)

    def send_email(self, recipient, subject, body) -> None:
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = self.email
        msg['To'] = recipient

        self.login()
        self.server.send_message(msg)
        self.logout()

    def logout(self) -> bool:
        self.server.quit()
