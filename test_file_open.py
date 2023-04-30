import unittest
from unittest import mock


def get_file_text(filename):
    with open(filename) as file:
        return file.read()


class FileOpenTestCase(unittest.TestCase):
    def test_files(self):
        # для теста стандартной функции open() нужно использовать builtins.open
        with mock.patch("builtins.open", mock.mock_open(read_data="Hello world! \n")):
            file_contents = get_file_text("foo.txt")
            self.assertEqual(file_contents, "Hello world! \n")
