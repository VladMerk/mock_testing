"""
Напишите тест для класса Calculator,
который содержит метод add(), который принимает 2 числа и возвращает их сумму.
 Необходимо замокать метод add() таким образом, чтобы он возвращал значение 10,
а затем проверить, что результат вызова этого метода будет равен 10
(если передать ему значения 5 и 5).
"""
import unittest
from unittest.mock import MagicMock, patch
from calculator import Calculator
import calculator


class CalculatorTestCase(unittest.TestCase):

    # def test_calculator_add_func(self):
    #     calc = MagicMock(spec=Calculator)
    #     calc.add.side_effect = {7: (3, 4), 9: (4, 5)}

    #     calc.divide.side_effect = ZeroDivisionError('division by zero')

    #     self.assertEqual(calc.add(3, 4), 7)
    #     calc.add.assert_called_once_with(3, 4)
    #     self.assertEqual(calc.add(4, 5), 9)

    #     with self.assertRaises(ZeroDivisionError):
    #         calc.divide(10, 0)
    pass
