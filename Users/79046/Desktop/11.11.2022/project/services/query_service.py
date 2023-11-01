import tinydb
from items import get_items
from parse import parse
from config import BASE_URL, DB_PATH
from report import report_cli_adhoc, report_csv_adhoc


def query_item(item: str, category_name: str, seve_to_file=False):
    db = tinydb.TinyDB(DB_PATH)
    table = db.table('categories')
    categories = table.get(doc_id=1)
    
    category_path = categories.get(category_name, BASE_URL)
    parser = parse(category_path + '?q=' + item)
    
    results = get_items(parser)

    if seve_to_file:
        report_csv_adhoc(results, ['title', 'price', 'url', 'date', 'text'])

    report_cli_adhoc(results, ['title', 'price', 'url', 'date'])