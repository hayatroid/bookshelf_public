import json
import requests
from loguru import logger


def gen_books(isbns):
    books = []
    for isbn in isbns:
        try:
            url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}'
            fetched_book = requests.get(url).json()
            book = {}
            book['isbn'] = isbn
            book['title'] = fetched_book['items'][0]['volumeInfo']['title']
            book['thumbnail'] = fetched_book['items'][0]['volumeInfo']['imageLinks']['thumbnail']
            books.append(book)
            logger.info(f'Successfully fetched {isbn}')
        except Exception as e:
            logger.error(f'Failed to fetch {isbn}: {e.__class__.__name__}: {e}')
    return books


isbns = json.load(open('../isbns.json', 'r'))

result = {}
result['💤'] = gen_books(isbns['💤'])
result['🚧'] = gen_books(isbns['🚧'])
result['✅'] = gen_books(isbns['✅'])

with open('../books.json', 'w') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)
