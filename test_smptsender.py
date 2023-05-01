import unittest
from unittest.mock import patch

from smptsender import EmailSender


class TestEmailSender(unittest.TestCase):

    @patch('smtplib.SMTP')
    def test_constructor(self, mock_smtp):
        """тест конструктора класса"""
        email_sender = EmailSender('test@gmail.com', 'pass')
        self.assertEqual(email_sender.email, 'test@gmail.com')
        self.assertEqual(email_sender.password, 'pass')
        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        mock_smtp.return_value.starttls.assert_called_once_with()

    @patch('smtplib.SMTP')
    def test_login_func(self, mock_smtp):
        email_sender = EmailSender('test@gmail.com', 'pass')
        email_sender.login()
        mock_smtp.assert_called_once()
        mock_smtp.return_value.login.assert_called_once_with('test@gmail.com', 'pass')

    @patch('smtplib.SMTP')
    def test_logout_func(self, mock_smtp):
        email_sender = EmailSender('test@gmail.com', 'pass')
        email_sender.logout()
        # mock_smtp.assert_called_once()
        mock_smtp.return_value.quit.assert_called_once_with()

    @patch('smtplib.SMTP')
    def test_send_email_func(self, mock_smtp):
        email_sender = EmailSender('test@gmail.com', 'pass')

        recipient = 'to@gmail.com'
        subject = 'Test subject'
        body = 'Test body of email\n'

        email_sender.send_email(recipient, subject, body)

        # mock_smtp.return_value.send_message.assert_called_once()
        email_sender.server.send_message.assert_called_once()
        email_sender.server.login.assert_called_once()
        email_sender.server.quit.assert_called_once()
