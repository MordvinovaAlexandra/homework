
from parse import clean


    
    

    
def get_items(parser):
    item_elements = parser.find('div', {"class": "content_left"})
    item_elements = item_elements.find_all('div', {'class': 'list_info'})

    items = []
    for element in item_elements:
        title = element.find('a', {'class': 'list_title'}).get_text()
        price = element.find('div', {'class': 'list_price'}) or "не указана"
        url = element.find('a', {'class': 'list_title'})['href']
        text = element.find('p', {'class': 'list_text'}).get_text()
        date = element.find('span', {'class': 'list_data'}).get_text()

        items.append(
            {
            'title': clean(title),
            'price': clean(price),
            'url': clean(url),
            'text': clean(text),
            'date': clean(date)
            }
        )

    
    return items


def save_items(db, data):
    categories_table = db.table('categories')
    categories_table.insert(data)