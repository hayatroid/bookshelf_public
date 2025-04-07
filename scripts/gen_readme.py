import json


def gen_usage():
    return '''>[!NOTE]
> This Markdown is auto-generated from [`isbns.json`](./isbns.json).\\
> Don't edit this file directly; update [`isbns.json`](./isbns.json) and commit/push your changes.

> [!TIP]
> Hover to see the book title.'''


def gen_row(list):
    return '|' + '|'.join(list) + '|'


def gen_img(book):
    return f'<img title="{book['title']}" src="{book['thumbnail']}" />'


def gen_table(books, cols=8):
    rows = []
    rows.append(gen_row([''] * cols))
    rows.append(gen_row(['-'] * cols))
    for i in range(0, len(books), cols):
        rows.append(gen_row(map(gen_img, books[i : i + cols])))
    return '\n'.join(rows)


books = json.load(open('../books.json', 'r'))

result = '\n\n'.join([
    '# bookshelf_public',
    gen_usage(),

    '## 💤 Unread',
    gen_table(books['💤']),

    '## 🚧 Reading',
    gen_table(books['🚧']),

    '## ✅ Read',
    gen_table(books['✅']),
])

with open('../README.md', 'w') as f:
    f.write(result)
