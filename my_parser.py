import requests
from bs4 import BeautifulSoup


def get_habr_titles():
    # sourcery skip: for-append-to-extend, inline-immediately-returned-variable, list-comprehension
    url = 'https://habr.com/ru/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    titles = []
    for title in soup.find_all('a', class_='post__title_link'):
        titles.append(title.text)
    return titles
