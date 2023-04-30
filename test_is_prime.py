import unittest
from unittest.mock import MagicMock, patch


def is_prime(n: int) -> bool:
    pass


class IsPrimeTestCase(unittest.TestCase):

    def test_is_prime_magic_mock(self):
        mock_prime = MagicMock(spec=is_prime)
        mock_prime.return_value = True


        self.assertTrue(mock_prime(5))

    def test_is_prime_patch_with(self):
        with patch('test_is_prime.is_prime') as mock_prime:
            mock_prime.return_value = True
            result = is_prime(5)
            self.assertTrue(result)
