import unittest
from unittest import mock

import requests


class SomeClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def summ(self):
        return self.a + self.b

    def div(self):
        return 0 if self.b == 0 else self.a / self.b


def get_response_status(url):
    response = requests.get(url)
    return response.status_code


def get_json(url):
    response = requests.get(url)
    return response.json()


def mock_response_func(url):
    mock_response = mock.MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"ok": True}
    return mock_response


@mock.patch("requests.get", side_effect=mock_response_func)
class SomeClassTestCase(unittest.TestCase):
    def test_mock_requests_status(self, mock_get):
        url = "https://ya.ru"

        self.assertEqual(get_response_status(url), 200)

    def test_mock_json_requests(self, mock_requests):
        url = "htts://ya.ru"

        self.assertEqual(get_json(url), {"ok": True})


if __name__ == "__main__":
    unittest.main()
