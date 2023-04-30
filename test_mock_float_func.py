import unittest
from unittest.mock import MagicMock, patch
import builtins

"""
Напишите тест для функции divide_numbers(a, b),
которая принимает 2 числа и возвращает результат их деления.
При этом необходимо замокать функцию float() таким образом,
чтобы она возвращала 2.5, а затем проверить,
что результат функции divide_numbers() будет равен 10
(если передать ей значения 25 и 2).
"""


def divide_numbers(a: int | float, b: int | float):
    return a / float(b)


class FloatDivideNumbersTestCase(unittest.TestCase):
    def test_divide_numbers_with(self):
        mock_float = MagicMock(return_value=2.5)
        with patch("builtins.float", mock_float):
            self.assertEqual(divide_numbers(25, 2), 10)

    @patch("builtins.float", return_value=2.5)
    def test_divide_numbers_decor(self, mock_float):
        self.assertEqual(divide_numbers(25, 2), 10)

    def test_divide_numbers_func(self):
        mock_float = MagicMock(return_value=2.5)

        builtins.float = mock_float

        self.assertEqual(divide_numbers(25, 2), 10)
