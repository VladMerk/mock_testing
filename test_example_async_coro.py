import random
import unittest

from aiohttp import ClientSession
from asynctest import CoroutineMock, patch


async def get_random_photo_url():
    while True:
        async with ClientSession() as session:
            async with session.get("random.photos") as resp:
                json = await resp.json()
        if photos := json["photos"]:
            return random.choice(photos)["img_src"]


class MyAsyncTestCase(unittest.IsolatedAsyncioTestCase):
    @patch("aiohttp.ClientSession.get")
    async def test_call_api_again_if_photos_not_found(self, mock_get):
        mock_get.return_value.__aenter__.return_value.json = CoroutineMock(
            side_effect=[{"photos": []}, {"photos": [{"img_src": "a.jpg"}]}]
        )

        image_url = await get_random_photo_url()

        assert mock_get.call_count == 2
        assert mock_get.return_value.__aenter__.return_value.json.call_count == 2
        assert image_url == "a.jpg"
