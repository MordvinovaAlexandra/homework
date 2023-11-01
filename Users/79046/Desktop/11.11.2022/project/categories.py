import tinydb

def get_categories(parser):
    category_elements = parser.find_all('div', { "class": "cat_list"})

    category_links = []
    for element in category_elements:
        category_links.append(element.find('a'))

    categories = {}
    for link in category_links:
        categories[link.get_text()] = link.attrs['href']

    return categories


def save_categories(db, data):
    categories_table = db.table('categories')
    categories_table.insert(data)