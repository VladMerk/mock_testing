from unittest import TestCase, mock

from my_parser import get_habr_titles


class TestGetHabrTitles(TestCase):

    @mock.patch('requests.get')
    def test_get_habr_titles(self, mock_get):
        mock_get.return_value.content = """
            <html>
                <body>
                    <a class="post__title_link">Title 1</a>
                    <a class="post__title_link">Title 2</a>
                    <a class="post__title_link">Title 3</a>
                </body>
            </html>
        """
        expected_titles = ['Title 1', 'Title 2', 'Title 3']
        self.assertEqual(get_habr_titles(), expected_titles)
