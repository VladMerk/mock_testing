"""
Напишите тест для функции get_url(url),
которая делает GET запрос к указанному URL
и возвращает содержимое страницы.
При этом необходимо замокать библиотеку requests таким образом,
чтобы вызов функции requests.get() возвращал объект с атрибутом text,
который в свою очередь возвращает строку "Hello, World!".
Затем нужно проверить,
что результат функции get_url() равен этой строке.
"""
import unittest
import requests

from unittest.mock import MagicMock, patch


def get_url(url: str):
    response = requests.get(url)
    return response.text


class RequestsMockTestCase(unittest.TestCase):
    def test_request_response_text_func(self):
        mock_response = MagicMock()
        mock_response.text = "Hello world! \n"

        mock_request = MagicMock()
        mock_request.get.return_value = mock_response

        requests.get = mock_request.get

        self.assertEqual(get_url("https://google.com"), "Hello world! \n")

    def test_request_response_text_with(self):
        with patch("requests.get") as mock_requests:
            mock_response = MagicMock()
            mock_response.text = "Hello world"

            mock_requests.return_value = mock_response

            self.assertEqual(get_url("google.com"), "Hello world")

    @patch("requests.get")
    def test_requests_response_text_decor(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = "hello world"

        mock_get.return_value = mock_response

        self.assertEqual(get_url("google.com"), "hello world")

    def test_requests_response_text_magic_mock(self):
        mock_response = MagicMock()
        mock_response.text = "Hello world"

        requests.get = MagicMock(return_value=mock_response)

        self.assertEqual(get_url("google.com"), "Hello world")
