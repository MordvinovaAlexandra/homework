import tinydb
from categories import save_categories, get_categories
from parse import parse
from config import BASE_URL, DB_PATH

db = tinydb.TinyDB(DB_PATH)
db.drop_tables()

parser = parse(BASE_URL)
categories = get_categories(parser)
save_categories(db, categories)
