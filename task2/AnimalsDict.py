import bs4
import requests


def animals_adding(animals_dict, url):
    session = requests.Session()
    session.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                     'like Gecko) Chrome/99.0.4844.74 Safari/537.36',
                       'Accept-Language': 'ru',
                       'Connection': 'close'}
    res = session.get(url=url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    for animal in soup.select_one('div.mw-category.mw-category-columns').select('a'):
        if animal.get('title')[0].upper() in animals_dict.keys():
            animals_dict[animal.get('title')[0].upper()].append(animal.get('title'))
        else:
            animals_dict[animal.get('title')[0].upper()] = [animal.get('title')]
    for page in soup.select_one('div[id="mw-pages"]').select('a'):
        if page.text == 'Следующая страница':
            animals_dict = animals_adding(animals_dict, 'https://ru.wikipedia.org/' + page.get('href'))
            return animals_dict
        else:
            continue
