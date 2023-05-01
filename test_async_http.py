import unittest

import aiohttp
from asynctest import CoroutineMock, patch


async def get_data(url):  # sourcery skip: instance-method-first-arg-name
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


class MyAsyncTestCase(unittest.IsolatedAsyncioTestCase):
    @patch("aiohttp.ClientSession.get")
    async def test_get_data(self, mock_get):
        url = "https://ya.ru"
        mock_get.status_code = 200
        mock_get.return_value.__aenter__.return_value.json = CoroutineMock(
            side_effect=[{"ok": True}]
        )

        expected_result = await get_data(url)

        self.assertEqual({"ok": True}, expected_result)
