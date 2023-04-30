import unittest
import datetime

from unittest import mock


def is_weekend():
    return datetime.datetime.now().weekday() in {5, 6}


class IsWeekendTestCase(unittest.TestCase):
    def test_is_weekend_func(self):
        mock_weekend = mock.MagicMock(spec=datetime.datetime)
        mock_weekend.now.return_value.weekday.return_value = 6

        datetime.datetime = mock_weekend

        self.assertEqual(is_weekend(), True)

    @mock.patch("datetime.datetime")
    def test_is_weekend_patch_func(self, date_mock):
        mock_now = mock.MagicMock()
        mock_now.weekday.side_effect = [0, 5]  # передаем 2 значения для теста дня
        date_mock.now.return_value = mock_now

        self.assertEqual(is_weekend(), False)  # реакция на 0
        self.assertEqual(is_weekend(), True)  # реакция на 6

    def test_is_weekend_patch_manager(self):
        with mock.patch("datetime.datetime") as mock_datetime:
            mock_now = mock.MagicMock()
            mock_datetime.now.return_value = mock_now
            # mock_now.weekday.return_value = 6
            mock_now.weekday.side_effect = {0, 3, 5, 6}
            self.assertFalse(is_weekend())
            self.assertFalse(is_weekend())
            self.assertTrue(is_weekend())
            self.assertTrue(is_weekend())
