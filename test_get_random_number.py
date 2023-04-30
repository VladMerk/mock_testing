import unittest
import random
from unittest import mock


def get_random_number(n):
    return random.randint(0, n)


class RandomNumberTestCase(unittest.TestCase):
    def test_get_random_number(self):
        mock_randint = mock.MagicMock(spec=random.randint)
        mock_randint.return_value = 5

        random.randint = mock_randint

        self.assertEqual(get_random_number(5), 5)

    @mock.patch("random.randint", return_value=5)
    def test_patch_random_number(self, mock_random):
        self.assertEqual(get_random_number(5), 5)

    def test_context_patch_random_number(self):
        with mock.patch("random.randint", return_value=4):
            self.assertTrue(get_random_number(5), 4)
